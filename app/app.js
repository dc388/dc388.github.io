/* LUFT · Asistencia — PWA para trabajadores (iPhone/Android web).
 *
 * Reutiliza EXACTAMENTE el mismo backend que la app Android:
 *   - enroll_device  : registra este navegador como "dispositivo" con una
 *                      llave ECDSA P-256 generada por WebCrypto (no sale del
 *                      dispositivo). El servidor ya acepta firma "raw" de 64
 *                      bytes, que es justo lo que produce WebCrypto.
 *   - punch_register : la checada se firma igual que en Android (payload
 *                      `checada.v2` con la ubicacion adentro), asi el servidor
 *                      aplica la MISMA geocerca y la misma verificacion.
 *
 * Sin rastreo oculto: la ubicacion se pide solo al momento de checar.
 */
'use strict';

const SUPABASE_URL = 'https://lsduggmuwbvrudpfcgtm.supabase.co';
const ANON_KEY =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxzZHVnZ211d2J2cnVkcGZjZ3RtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODc3NTc2NTIsImV4cCI6MjEwMzMzMzY1Mn0.lyRwNkwnzvwN6EN1j35VFlzgBeii8AWicNZaB1MfxGw';
const APP_VERSION = 'pwa-0.1.0';

// ---------- utilidades ----------
const $ = (id) => document.getElementById(id);
const enc = new TextEncoder();
const uuid = () => (crypto.randomUUID ? crypto.randomUUID()
  : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
      const r = (Math.random() * 16) | 0; return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16); }));
const bufToB64 = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)));
const f6 = (n) => (n == null ? '' : Number(n).toFixed(6));
const f1 = (n) => (n == null ? '' : Number(n).toFixed(1));

function show(screen) {
  ['loading', 'enroll', 'acuerdo', 'biometrico', 'selfie', 'enrolar-rostro', 'home', 'result', 'permisos', 'privacidad'].forEach((s) => { $(s).hidden = s !== screen; });
}
function busy(on, txt) { $('busy').hidden = !on; if (txt) $('busy-txt').textContent = txt; }

// ---------- almacenamiento ----------
const store = {
  get(k, d) { try { const v = localStorage.getItem('luft.' + k); return v ? JSON.parse(v) : d; } catch { return d; } },
  set(k, v) { try { localStorage.setItem('luft.' + k, JSON.stringify(v)); } catch {} },
  del(k) { try { localStorage.removeItem('luft.' + k); } catch {} },
};

// IndexedDB minimo, para guardar el par de llaves (CryptoKey) y la cola offline.
function idb() {
  return new Promise((res, rej) => {
    const r = indexedDB.open('luft', 1);
    r.onupgradeneeded = () => r.result.createObjectStore('kv');
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
  });
}
async function idbGet(k) { const db = await idb(); return new Promise((res, rej) => {
  const t = db.transaction('kv').objectStore('kv').get(k); t.onsuccess = () => res(t.result); t.onerror = () => rej(t.error); }); }
async function idbSet(k, v) { const db = await idb(); return new Promise((res, rej) => {
  const t = db.transaction('kv', 'readwrite').objectStore('kv').put(v, k); t.onsuccess = () => res(); t.onerror = () => rej(t.error); }); }

// ---------- capacidades del dispositivo (sin fingir) ----------
function deviceCapabilities() {
  const ua = navigator.userAgent;
  const iOS = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const android = /Android/.test(ua);
  const standalone = window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
  return {
    os: iOS ? 'iOS' : android ? 'Android' : 'Otro',
    browser: /CriOS/.test(ua) ? 'Chrome iOS' : /FxiOS/.test(ua) ? 'Firefox iOS'
      : /Safari/.test(ua) && iOS ? 'Safari' : /Chrome/.test(ua) ? 'Chrome' : 'Navegador',
    pwaInstalled: standalone,
    camera: !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia),
    gps: 'geolocation' in navigator,
    webauthn: !!window.PublicKeyCredential,
    passkeys: !!(window.PublicKeyCredential && PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable),
    notifications: 'Notification' in window,
    serviceWorker: 'serviceWorker' in navigator,
    offline: 'indexedDB' in window && 'caches' in window,
    backgroundLocation: !iOS && android && standalone ? 'limitado' : 'no-pwa', // honesto: iOS PWA no puede
    backgroundSync: 'serviceWorker' in navigator && 'SyncManager' in window,
    secureContext: window.isSecureContext,
  };
}

// ---------- dispositivo: id + llave ECDSA ----------
async function ensureDevice() {
  let id = store.get('deviceId');
  if (!id) { id = uuid(); store.set('deviceId', id); }
  let pair = await idbGet('keypair');
  if (!pair) {
    // No exportable: la privada no sale del dispositivo.
    pair = await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign', 'verify']);
    await idbSet('keypair', pair);
  }
  let spki;
  try { spki = bufToB64(await crypto.subtle.exportKey('spki', pair.publicKey)); }
  catch (e) {
    // Algunos navegadores exigen extractable para exportar la publica: se
    // regenera un par extractable (la privada sigue guardada solo aqui).
    pair = await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
    await idbSet('keypair', pair);
    spki = bufToB64(await crypto.subtle.exportKey('spki', pair.publicKey));
  }
  return { id, pair, spki };
}
async function signPayload(pair, payload) {
  const raw = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, pair.privateKey, enc.encode(payload));
  return bufToB64(raw); // 64 bytes r||s — el servidor lo acepta tal cual
}

// ---------- red / sesion ----------
// Toda llamada lleva un tope de tiempo (AbortController). Sin esto, una señal
// debil de obra deja el fetch colgado para siempre y la checada nunca cae a la
// cola offline: el trabajador se queda mirando "Registrando…". Al expirar, lanza
// (AbortError) para que el llamador decida; punch() lo aprovecha para encolar.
async function api(path, { method = 'POST', body, auth, timeoutMs = 12000 } = {}) {
  const headers = { 'Content-Type': 'application/json', apikey: ANON_KEY };
  if (auth) headers.Authorization = 'Bearer ' + auth;
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), timeoutMs);
  try {
    const res = await fetch(SUPABASE_URL + path, {
      method, headers, body: body ? JSON.stringify(body) : undefined, signal: ctl.signal,
    });
    const text = await res.text();
    let data; try { data = text ? JSON.parse(text) : null; } catch { data = text; }
    return { ok: res.ok, status: res.status, data };
  } finally { clearTimeout(timer); }
}
async function accessToken() {
  const s = store.get('session');
  if (!s) return null;
  // Solo intentamos refrescar si el token esta por vencer Y hay red. Offline o con
  // señal mala usamos el token actual sin tocar la red (arranque y checada rapidos).
  if (s.expires_at && Date.now() / 1000 > s.expires_at - 60 && navigator.onLine) {
    try {
      const r = await api('/auth/v1/token?grant_type=refresh_token', { body: { refresh_token: s.refresh_token } });
      if (r.ok && r.data && r.data.access_token) {
        const ns = { ...s, access_token: r.data.access_token, refresh_token: r.data.refresh_token,
          expires_at: r.data.expires_at || Math.floor(Date.now() / 1000) + (r.data.expires_in || 3600) };
        store.set('session', ns); return ns.access_token;
      }
    } catch { /* red mala / timeout: no lanzamos, usamos el token actual */ }
    return s.access_token; // ultimo recurso
  }
  return s.access_token;
}

// ---------- registro por codigo ----------
async function enroll(code) {
  busy(true, 'Registrando…');
  try {
    const dev = await ensureDevice();
    const cap = deviceCapabilities();
    const r = await api('/functions/v1/enroll_device', { body: {
      code, device_id: dev.id, public_key: dev.spki,
      device_model: cap.browser + ' / ' + cap.os, os_version: cap.os, app_version: APP_VERSION,
    }});
    if (!r.ok || !r.data || !r.data.access_token) {
      return { ok: false, msg: (r.data && r.data.error) || 'Código inválido o vencido. Pide otro a RH.' };
    }
    const d = r.data;
    store.set('session', {
      access_token: d.access_token, refresh_token: d.refresh_token,
      expires_at: Math.floor(Date.now() / 1000) + (d.expires_in || 3600),
      employee: d.employee,
    });
    return { ok: true };
  } catch (e) { return { ok: false, msg: 'No se pudo registrar: ' + (e.message || e) }; }
  finally { busy(false); }
}

// ---------- acuerdo laboral + aviso de privacidad ----------
let AC = null; // documentos vigentes en memoria

async function gateAgreements() {
  // Decide si mostrar el acuerdo o pasar a la pantalla principal.
  // Offline: no hay forma de consultar el estado ni tendria caso bloquear la
  // entrada por eso (una falla de red no es falta). Vamos directo a Home; al
  // reconectar, el proximo arranque lo revisa.
  if (!navigator.onLine) { renderHome(); return; }
  try {
    const token = await accessToken();
    const r = await api('/rest/v1/rpc/agreements_status', { body: {}, auth: token });
    if (!r.ok || !r.data || r.data.error) { renderHome(); return; } // no bloquear por fallo de red
    AC = r.data;
    if (AC.needs_acceptance && AC.labor && AC.privacy) renderAcuerdo();
    else gateBiometric();
  } catch { renderHome(); } // timeout/red mala: tampoco bloquea
}

// El consentimiento biometrico es SEPARADO y OPCIONAL: se ofrece una sola vez por
// version, no bloquea la entrada, y declinar no es sancion. Solo aparece si hay
// un documento biometrico vigente sobre el que este trabajador aun no decide.
function gateBiometric() {
  if (AC && AC.biometric && !AC.biometric.decision) { renderBiometrico(); return; }
  renderHome();
}

function renderBiometrico() {
  $('bio-title').textContent = AC.biometric.title || 'Reconocimiento facial';
  $('bio-legal').hidden = !AC.biometric.legal_review_required;
  $('bio-doc').innerHTML = escapeHtml(AC.biometric.body);
  document.querySelectorAll('#bio-checks input').forEach((c) => { c.checked = false; });
  $('bio-btn').disabled = true;
  $('bio-msg').textContent = '';
  show('biometrico');
}

function bioChecks() {
  const flags = {};
  document.querySelectorAll('#bio-checks input').forEach((c) => { flags[c.dataset.k] = c.checked; });
  return flags;
}

// decision: 'granted' (autoriza, exige las 3 casillas) o 'declined' (metodo alterno).
async function decideBiometric(decision) {
  const flags = bioChecks();
  if (decision === 'granted' && !Object.values(flags).every(Boolean)) return;
  busy(true, decision === 'granted' ? 'Guardando autorización…' : 'Guardando…');
  try {
    const dev = await ensureDevice();
    const cap = deviceCapabilities();
    const token = await accessToken();
    const r = await api('/rest/v1/rpc/accept_biometric', { auth: token, body: {
      p_biometric_agreement_id: AC.biometric.id, p_decision: decision,
      p_device_id: dev.id, p_platform: cap.os + '-' + (cap.pwaInstalled ? 'PWA' : 'web'),
      p_app_version: APP_VERSION, p_auth_method: 'code',
      p_consent_flags: decision === 'granted' ? flags : { decision: 'declined' },
    }});
    if (!r.ok) {
      $('bio-msg').className = 'msg err';
      $('bio-msg').textContent = (r.data && r.data.message) || 'No se pudo guardar. Intenta de nuevo.';
      return;
    }
    store.set('bioGranted', decision === 'granted');
    // Si autoriza y el telefono tiene biometria del sistema, ofrecemos enrolar
    // Face ID/Touch ID como verificacion de persona presente al checar. Es
    // opcional: si la rechaza o falla, la asistencia sigue por el metodo alterno.
    if (decision === 'granted' && await passkeyAvailable()) {
      busy(true, 'Configurando Face ID…');
      const pk = await enrollPasskey();
      store.set('passkey', pk.ok);
    }
    // Tras autorizar, si aún no tiene su rostro enrolado, va directo a registrarlo
    // (una sola vez). De ahí en adelante checa con la cara.
    if (decision === 'granted') {
      busy(true, 'Verificando registro de rostro…');
      await loadFaceStatus();
      busy(false);
      if (FACE && FACE.granted && !FACE.enrolled) { renderEnrolar(); return; }
    }
    renderHome();
  } finally { busy(false); }
}

function renderAcuerdo() {
  $('ac-title').textContent = AC.labor.title || 'Acuerdo de control de asistencia';
  $('ac-legal').hidden = !(AC.labor.legal_review_required || AC.privacy.legal_review_required);
  $('ac-doc').innerHTML =
    `<h4>${escapeHtml(AC.labor.title)}</h4>${escapeHtml(AC.labor.body)}` +
    `<h4>${escapeHtml(AC.privacy.title)}</h4>${escapeHtml(AC.privacy.body)}`;
  // Reset casillas (nunca premarcadas).
  document.querySelectorAll('#ac-checks input').forEach((c) => { c.checked = false; });
  $('ac-btn').disabled = true;
  $('ac-msg').textContent = '';
  show('acuerdo');
}

function acChecks() {
  const flags = {};
  document.querySelectorAll('#ac-checks input').forEach((c) => { flags[c.dataset.k] = c.checked; });
  return flags;
}

async function acceptAgreement() {
  const flags = acChecks();
  if (!Object.values(flags).every(Boolean)) return;
  busy(true, 'Guardando aceptación…');
  try {
    const dev = await ensureDevice();
    const cap = deviceCapabilities();
    const token = await accessToken();
    const r = await api('/rest/v1/rpc/accept_agreement', { auth: token, body: {
      p_labor_agreement_id: AC.labor.id, p_privacy_notice_id: AC.privacy.id,
      p_device_id: dev.id, p_platform: cap.os + '-' + (cap.pwaInstalled ? 'PWA' : 'web'),
      p_app_version: APP_VERSION, p_auth_method: 'code', p_consent_flags: flags,
    }});
    if (!r.ok) { $('ac-msg').className = 'msg err'; $('ac-msg').textContent = (r.data && r.data.message) || 'No se pudo guardar. Intenta de nuevo.'; return; }
    // Tras labor+privacy, re-consultamos el estado para saber si falta ofrecer el
    // consentimiento biometrico (documento aparte).
    const token2 = await accessToken();
    const rs = await api('/rest/v1/rpc/agreements_status', { body: {}, auth: token2 });
    if (rs.ok && rs.data && !rs.data.error) AC = rs.data;
    gateBiometric();
  } finally { busy(false); }
}

function escapeHtml(s) { return String(s == null ? '' : s).replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c])); }

// ---------- Face ID / Touch ID del dispositivo (WebAuthn) ----------
// Distincion legal (Pantalla 3): esto es biometria del SISTEMA OPERATIVO usada
// para verificar que hay una persona presente al checar. LUFT NO recibe el rostro
// ni la huella: el SO hace la biometria y solo entrega una firma (asercion). Es
// distinto del reconocimiento facial propio de LUFT. Aqui funciona como reto de
// "persona presente" antes de una checada; si falla o no existe, NO bloquea la
// asistencia (una falla tecnica no es falta) — se marca para revision.
const b64urlToBuf = (s) => {
  s = s.replace(/-/g, '+').replace(/_/g, '/');
  const pad = s.length % 4 ? 4 - (s.length % 4) : 0; s += '='.repeat(pad);
  const bin = atob(s); const u = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
  return u.buffer;
};
const bufToB64url = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)))
  .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

async function passkeyAvailable() {
  try {
    return !!(window.PublicKeyCredential &&
      await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable());
  } catch { return false; }
}

async function enrollPasskey() {
  if (!(await passkeyAvailable())) return { ok: false, reason: 'no-soportado' };
  const s = store.get('session'); const emp = (s && s.employee) || {};
  const dev = await ensureDevice();
  const challenge = crypto.getRandomValues(new Uint8Array(32));
  const userId = enc.encode(String(emp.id || dev.id)).slice(0, 64);
  try {
    const cred = await navigator.credentials.create({ publicKey: {
      challenge,
      rp: { name: 'LUFT Asistencia', id: location.hostname },
      user: {
        id: userId,
        name: emp.employee_number || emp.first_name || 'trabajador',
        displayName: ((emp.first_name || '') + ' ' + (emp.last_name || '')).trim() || 'Trabajador',
      },
      pubKeyCredParams: [{ type: 'public-key', alg: -7 }, { type: 'public-key', alg: -257 }],
      authenticatorSelection: { authenticatorAttachment: 'platform', userVerification: 'required', residentKey: 'preferred' },
      timeout: 60000, attestation: 'none',
    }});
    if (!cred) return { ok: false, reason: 'cancelado' };

    // La llave PUBLICA en SPKI, para que el servidor pueda verificar las
    // aserciones. getPublicKey() evita tener que parsear el attestationObject
    // (CBOR) en el servidor. Requiere iOS 16+/Chrome 85+.
    const resp = cred.response;
    if (!resp.getPublicKey) return { ok: false, reason: 'sin-getPublicKey' };
    const spki = resp.getPublicKey();
    const alg = resp.getPublicKeyAlgorithm ? resp.getPublicKeyAlgorithm() : -7;
    if (!spki) return { ok: false, reason: 'sin-llave-publica' };

    const credId = bufToB64url(cred.rawId);
    const token = await accessToken();
    const r = await api('/functions/v1/webauthn_register', { auth: token, body: {
      credential_id: credId, public_key_spki: bufToB64url(spki), alg, device_id: dev.id,
    }});
    if (!r.ok) return { ok: false, reason: (r.data && r.data.error) || 'registro-servidor' };

    await idbSet('passkeyId', credId);
    return { ok: true };
  } catch (e) { return { ok: false, reason: e.name || 'error' }; }
}

// Pide un reto al servidor para ESTA operacion, lo firma con el passkey y
// devuelve la asercion lista para mandar en la checada. null si no aplica o
// falla (nunca bloquea la asistencia).
async function assertPasskey(opId) {
  const idb64 = await idbGet('passkeyId');
  if (!idb64) return null;
  try {
    const token = await accessToken();
    const opt = await api('/functions/v1/webauthn_auth_options', { auth: token, body: { client_operation_id: opId } });
    if (!opt.ok || !opt.data || !opt.data.challenge) return null;
    const d = opt.data;
    const assertion = await navigator.credentials.get({ publicKey: {
      challenge: b64urlToBuf(d.challenge),
      rpId: d.rpId || location.hostname,
      timeout: d.timeout || 60000,
      userVerification: d.userVerification || 'required',
      allowCredentials: (d.allowCredentials || [{ id: idb64, type: 'public-key' }])
        .map((c) => ({ type: 'public-key', id: b64urlToBuf(c.id) })),
    }});
    if (!assertion) return null;
    const a = assertion.response;
    return {
      credential_id: bufToB64url(assertion.rawId),
      authenticator_data: bufToB64url(a.authenticatorData),
      client_data_json: bufToB64url(a.clientDataJSON),
      signature: bufToB64url(a.signature),
    };
  } catch (e) { return null; }
}

// ---------- ubicacion ----------
// El GPS NO necesita internet: funciona en obra sin señal. Pero el fix de alta
// precision puede tardar o expirar ahi; entonces reintentamos con baja precision
// (torres/wifi cacheado) antes de rendirnos, para no bloquear la checada por un
// fix lento. La precision reportada sigue siendo la real: el servidor decide la
// geocerca con ese margen. Un permiso DENEGADO no se reintenta (fallaria igual).
function getLocation() {
  const fix = (hi) => new Promise((resolve) => {
    navigator.geolocation.getCurrentPosition(
      (p) => resolve({ status: 'AUTORIZADA', lat: p.coords.latitude, lng: p.coords.longitude, acc: p.coords.accuracy }),
      (err) => resolve({ status: err.code === 1 ? 'DENEGADA' : 'NO_DISPONIBLE', error: err.message, code: err.code }),
      { enableHighAccuracy: hi, timeout: hi ? 12000 : 8000, maximumAge: hi ? 0 : 30000 },
    );
  });
  return (async () => {
    if (!navigator.geolocation) return { status: 'NO_DISPONIBLE' };
    const r = await fix(true);
    if (r.status === 'NO_DISPONIBLE') {
      const r2 = await fix(false);
      if (r2.status === 'AUTORIZADA') return r2;
      return r;
    }
    // Un primer fix por torre/wifi llega con cientos o miles de metros de error
    // y es INUTIL para una geocerca de 250 m. El 11 de septiembre N1-001 mando
    // cuatro checadas con acc = 2000 m: el servidor midio 587 m al Modulo y las
    // rechazo por "fuera de la geocerca", cuando con ese error la persona bien
    // podia estar adentro. El GPS converge en segundos si se le da tiempo, asi
    // que en vez de mandar el primer fix se espera un rato a uno mejor.
    if (r.status === 'AUTORIZADA' && r.acc != null && r.acc > ACC_BUENA_M) {
      busy(true, 'Afinando tu ubicación…');
      return await afinarUbicacion(r, 15000);
    }
    return r;
  })();
}

// Error de GPS con el que ya se puede decidir una geocerca de 250 m sin apostar.
const ACC_BUENA_M = 100;

// Sigue escuchando al GPS hasta `ms` y devuelve la MEJOR lectura (la de menor
// error). Corta antes si llega una suficientemente buena.
function afinarUbicacion(inicial, ms) {
  return new Promise((resolve) => {
    if (!navigator.geolocation.watchPosition) return resolve(inicial);
    let mejor = inicial, id = null, temporizador = null, cerrado = false;
    const cerrar = () => {
      if (cerrado) return;
      cerrado = true;
      try { if (id != null) navigator.geolocation.clearWatch(id); } catch (e) {}
      clearTimeout(temporizador);
      resolve(mejor);
    };
    try {
      id = navigator.geolocation.watchPosition(
        (p) => {
          const acc = p.coords.accuracy;
          if (acc != null && (mejor.acc == null || acc < mejor.acc)) {
            mejor = { status: 'AUTORIZADA', lat: p.coords.latitude, lng: p.coords.longitude, acc };
          }
          if (acc != null && acc <= ACC_BUENA_M) cerrar();
        },
        () => { /* un error aqui no quita la lectura que ya se tiene */ },
        { enableHighAccuracy: true, maximumAge: 0, timeout: ms },
      );
    } catch (e) { return resolve(inicial); }
    temporizador = setTimeout(cerrar, ms);
  });
}

// ---------- politica de checada de la empresa ----------
let POL = null; // { audit_photo_enabled, offsite_requires_photo, allow_offsite_punch }
async function loadPolicy() {
  try {
    const token = await accessToken();
    const r = await api('/rest/v1/rpc/attendance_policy', { body: {}, auth: token });
    if (r.ok && r.data && !r.data.error) POL = r.data;
  } catch { /* si falla, se checa sin foto: no bloquear por esto */ }
}

// ---------- reconocimiento facial: estado + enrolamiento ----------
// FACE = { granted, enrolled, consent_id, embedding_version }
let FACE = null;
async function loadFaceStatus() {
  try {
    const token = await accessToken();
    const r = await api('/rest/v1/rpc/face_status', { body: {}, auth: token });
    if (r.ok && r.data && !r.data.error) FACE = r.data;
  } catch { /* sin red: se resuelve en el próximo arranque con señal */ }
  return FACE;
}

let erStream = null;
function stopEr() { if (erStream) { try { erStream.getTracks().forEach((t) => t.stop()); } catch {} erStream = null; } }

// Enrolamiento: lee el rostro varias veces (una sola vez en la vida del empleado)
// y manda los vectores a enroll_face. La foto no se guarda; solo el vector.
async function renderEnrolar() {
  show('enrolar-rostro');
  const video = $('er-video'), prog = $('er-progreso'), btn = $('er-btn'), msg = $('er-msg');
  msg.textContent = ''; msg.className = 'msg'; btn.disabled = true;
  if (!(window.LuftFace && LuftFace.supported())) {
    const por = (window.LuftFace && LuftFace.faltante && LuftFace.faltante()) || null;
    msg.className = 'msg err';
    msg.textContent = por
      ? 'No se puede registrar el rostro aquí: ' + por + '.'
      : 'Este navegador no soporta el reconocimiento facial. Usa Safari o Chrome actualizado.';
    return;
  }
  prog.textContent = 'Encendiendo cámara…';
  try {
    erStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user', width: { ideal: 480 }, height: { ideal: 480 } }, audio: false });
    video.srcObject = erStream;
  } catch (e) { msg.className = 'msg err'; msg.textContent = 'No se pudo abrir la cámara. Actívala en Ajustes.'; return; }
  prog.textContent = 'Preparando el modelo (la 1ª vez baja 23 MB con señal)…';
  try {
    await LuftFace.ready(
      (recibido, total) => {
        const pct = Math.min(100, Math.round((recibido / total) * 100));
        prog.textContent = 'Descargando el modelo… ' + pct + '%  (solo la 1ª vez)';
      },
      // Cada etapa se dice en voz alta. Antes, el 100% de los atorones se veian
      // como "Preparando el modelo..." sin mas, aunque el modelo ni se hubiera
      // empezado a bajar.
      (txt) => { prog.textContent = txt; },
    );
  } catch (e) {
    msg.className = 'msg err';
    // El motivo REAL, no uno inventado: si se atoró abriendo el motor, decir
    // "revisa tu señal" manda a la persona a perseguir el problema equivocado.
    msg.textContent = 'No se pudo preparar el reconocimiento facial: ' +
      (e && e.message ? e.message : 'error desconocido') + '.';
    prog.textContent = 'Con señal (datos o wifi) vuelve a tocar “Reintentar”.';
    btn.disabled = false;
    btn.textContent = 'Reintentar';
    btn.onclick = () => { btn.textContent = 'Registrar mi rostro'; renderEnrolar(); };
    return;
  }
  prog.textContent = 'Listo. Toca “Registrar mi rostro”.';
  btn.textContent = 'Registrar mi rostro';
  btn.disabled = false;
  btn.onclick = capturarEnrolamiento;
}

async function capturarEnrolamiento() {
  const video = $('er-video'), prog = $('er-progreso'), btn = $('er-btn'), msg = $('er-msg');
  btn.disabled = true; msg.textContent = ''; msg.className = 'msg';
  const N = 4, captures = [];
  try {
    // UNA SOLA PASADA. La version anterior llamaba a leerRostroConfiable() por
    // cada una de las 4 capturas, y como esa funcion busca internamente hasta 10
    // lecturas, el enrolamiento pasaba de ~4 lecturas a hasta 40: se volvia
    // lentisimo y parecia trabado en "Capturando 4 de 4".
    //
    // Aqui se junta todo en un recorrido: se toman lecturas hasta reunir N que
    // pasen el piso de calidad, con un techo de intentos para no quedarse dando
    // vueltas. Se conserva lo que importaba —no guardar lecturas basura— sin el
    // costo de repetir la busqueda cuatro veces.
    //
    // El motivo del filtro sigue siendo el mismo: guardar un template de ruido
    // (enrolarse a contraluz o de lejos) bloquea a la persona TODOS los dias,
    // porque la checada, que si lee bien, nunca le coincide. Eso son los
    // "rostro no coincide (0.07)" del 11 de septiembre.
    const MAX_INTENTOS = 12;
    for (let i = 0; i < MAX_INTENTOS && captures.length < N; i++) {
      prog.textContent = 'Capturando ' + (captures.length + 1) + ' de ' + N + '… mira de frente';
      try {
        const r = await LuftFace.embed(video);
        if (r.quality >= MIN_CALIDAD_ROSTRO) {
          captures.push({ embedding: Array.from(r.vec), quality_score: r.quality });
          msg.textContent = '';
          await new Promise((res) => setTimeout(res, 250));
        } else {
          msg.className = 'msg';
          msg.textContent = 'Acércate un poco: se te ve muy lejos…';
          await new Promise((res) => setTimeout(res, 300));
        }
      } catch (e) {
        msg.className = 'msg';
        msg.textContent = (e.message || 'no se ve tu cara') + '…';
        await new Promise((res) => setTimeout(res, 300));
      }
    }
    if (captures.length < N) {
      throw new Error('no se pudo leer bien tu rostro; ponte de frente, con la luz dándote en la cara, y vuelve a intentar');
    }

    // Las 4 capturas son de la MISMA cara con segundos de diferencia: tienen que
    // parecerse mucho entre si. Si no se parecen, el promedio que calcula
    // enroll_face no es el rostro de nadie —es el centro de un ruido— y ese es
    // justo el template que despues no coincide con nada. Se revisa aqui porque
    // cada lectura pudo pasar su propio filtro y aun asi no concordar entre si.
    let peor = 1;
    for (let i = 0; i < captures.length; i++) {
      for (let j = i + 1; j < captures.length; j++) {
        const s = LuftFace.cosine(captures[i].embedding, captures[j].embedding);
        if (s < peor) peor = s;
      }
    }
    if (peor < MIN_ACUERDO_LECTURAS) {
      msg.className = 'msg err';
      msg.textContent = 'Las capturas salieron muy distintas entre sí (contraluz o movimiento). ' +
        'Ponte de frente, con la luz dándote en la cara, y vuelve a intentar.';
      prog.textContent = '';
      btn.disabled = false;
      return;
    }

    prog.textContent = 'Guardando tu rostro en la plataforma…';
    if (!FACE || !FACE.consent_id) await loadFaceStatus();
    const token = await accessToken();
    const r = await api('/functions/v1/enroll_face', { auth: token, body: {
      captures,
      embedding_version: (FACE && FACE.embedding_version) || LuftFace.VERSION,
      consent_id: FACE && FACE.consent_id,
    }});
    if (!r.ok) { msg.className = 'msg err'; msg.textContent = (r.data && (r.data.error || r.data.message)) || 'No se pudo guardar. Intenta de nuevo.'; btn.disabled = false; return; }
    if (FACE) FACE.enrolled = true;
    stopEr();
    showResult('ok', 'Rostro registrado', 'Listo. A partir de ahora checas con tu cara.');
  } catch (e) { msg.className = 'msg err'; msg.textContent = e.message || 'Error al registrar el rostro.'; btn.disabled = false; }
}

// Pide un reto de vida al servidor y devuelve su id (o null).
async function pedirRetoVida() {
  try {
    const token = await accessToken();
    const r = await api('/functions/v1/liveness_challenge', { auth: token, body: {} });
    if (r.ok && r.data && r.data.challenge_id) return r.data.challenge_id;
  } catch { /* sin reto: la checada quedará a revisión, no bloquea la vida real */ }
  return null;
}

// Reto de vida "acércate": mide que el rostro CREZCA (movimiento real de la
// persona). Una foto estática no cambia de tamaño. true si lo detecta a tiempo.
async function retoAcercarse(video, msg) {
  msg.className = 'msg'; msg.textContent = 'Acerca tu cara despacio a la cámara…';
  let base = null; const t0 = Date.now();
  // 6 s y crecimiento de 1.25x: suficiente para distinguir a una persona de una
  // foto estatica, sin pelear con quien sostiene el telefono a distancia fija.
  // NO bloquea: si no se detecta, la checada igual se envia y el servidor la
  // manda a revision (ver capturarRostroChecada / migracion 0064).
  while (Date.now() - t0 < 6000) {
    let box = null;
    try { box = await LuftFace.detectBox(video); } catch {}
    if (box) {
      const area = box.w * box.h;
      if (base === null) base = area;
      if (area >= base * 1.25) { msg.textContent = '¡Listo!'; return true; }
      if (area < base) base = area; // si se aleja, baja la referencia
    }
    await new Promise((res) => setTimeout(res, 120));
  }
  return false;
}

// Captura el rostro para la checada: reto de vida + UN vector (el match 1:1 lo
// hace el servidor).
//
// Devuelve:
//   { vec, challengeId, ... }  se leyo el rostro
//   SIN_MOTOR                  este telefono NO PUEDE con el reconocimiento
//   null                       el motor si puede, pero no se logro la lectura
//
// La diferencia entre los dos ultimos es todo el candado. Un telefono viejo que
// no carga el modelo se queda SIN PODER CHECAR NUNCA si se le trata igual que a
// quien tapa la camara: con el rostro ya enrolado, la app se lo exige en cada
// checada y el no puede darlo. Por eso el primer caso cae al metodo alterno
// (firma del dispositivo + selfie de evidencia) y el segundo sigue bloqueando:
// si cualquier fallo de lectura abriera la salida, taparse la camara seria la
// forma de saltarse el reconocimiento.
const SIN_MOTOR = 'sin-motor';
async function capturarRostroChecada() {
  const video = $('selfie-video'), msg = $('selfie-msg'), title = $('selfie-title');
  $('selfie-take').hidden = true; $('selfie-skip').hidden = true;
  // Equipo sin WebAssembly / sin IndexedDB / sin camara: no hay motor que
  // cargar. Se sabe ANTES de encender la camara, sin hacerlo esperar.
  if (!(window.LuftFace && LuftFace.supported())) return SIN_MOTOR;
  title.textContent = 'Reconociendo tu rostro…';
  msg.className = 'msg'; msg.textContent = 'Un momento…';
  show('selfie');
  let stream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user', width: { ideal: 480 }, height: { ideal: 480 } }, audio: false });
    video.srcObject = stream;
  } catch (e) { $('selfie-take').hidden = false; return null; }
  const stop = () => { try { stream.getTracks().forEach((t) => t.stop()); } catch {} };
  // El modelo no carga en este equipo (memoria, WASM sin SIMD, navegador viejo).
  // No es que no se le vea la cara: es que aqui no se puede. Metodo alterno.
  try { await LuftFace.ready(); }
  catch (e) { stop(); $('selfie-take').hidden = false; return SIN_MOTOR; }

  // Gesto de vida (anti-foto): OBLIGATORIO —una foto estatica no crece de
  // tamano y no pasa—. Para que la gente legitima lo logre sin relajar el
  // candado, se dan DOS intentos con guia clara antes de pedir reintentar.
  let vivo = await retoAcercarse(video, msg);
  if (!vivo) {
    msg.className = 'msg'; msg.textContent = 'Acércate un poco más, de frente…';
    vivo = await retoAcercarse(video, msg);
  }
  if (!vivo) {
    stop(); $('selfie-take').hidden = false;
    msg.className = 'msg err';
    msg.textContent = 'No detecté que te acercaras. Toca de nuevo el botón y acerca el teléfono a tu cara.';
    return null;
  }

  // El reto de vida se pide AQUI, ya pasado el gesto y justo antes de leer el
  // rostro. Vive 20 s (company_settings.liveness_challenge_ttl_seconds) y el
  // gesto puede tardar 12 s entre sus dos intentos: pedirlo antes lo dejaba
  // vencido al llegar al envio, y el servidor rechazaba la checada con "reto de
  // vida vencido" (9 de 63 checadas los dias 10 y 11 de septiembre). Pedirlo
  // aqui no afloja nada —el token sirve contra el replay AL ENVIAR— y llega
  // fresco.
  const challengeId = await pedirRetoVida();

  msg.className = 'msg'; msg.textContent = 'Leyendo tu rostro…';
  const lectura = await leerRostroConfiable(video, msg);
  stop();
  $('selfie-take').hidden = false; // restaurar para la selfie de auditoría
  if (!lectura) return null;
  // Solo se llega aquí con el gesto logrado (vivo=true): el candado se mantiene.
  return { vec: lectura.vec, challengeId, livenessPassed: true, padScore: 1 };
}

// Cara demasiado chica en el cuadro: el recorte sale de pocos pixeles y el
// vector es ruido. 0.02 = la cara ocupa el 2% del cuadro; los enrolamientos
// reales de la plantilla andan en 0.35-0.74, asi que es un piso muy holgado
// que solo ataja basura.
const MIN_CALIDAD_ROSTRO = 0.02;
// Que tan de acuerdo tienen que estar entre si las lecturas para creerles.
const MIN_ACUERDO_LECTURAS = 0.55;
// Acuerdo tan alto entre dos lecturas seguidas que ya no vale la pena tomar mas.
// Dos lecturas buenas del mismo rostro se parecen muchisimo; las basura no
// llegan ni cerca (0.036-0.29 en los casos reales), asi que este atajo lo toma
// solo quien ya quedo bien leido.
const ACUERDO_SUFICIENTE = 0.80;

// Lee el rostro VARIAS veces y devuelve la lectura mas consistente, o null si
// ninguna lo es.
//
// Por que: `embed()` devuelve un vector aunque el cuadro este quemado por el
// sol, movido o con la cara a contraluz —y ese vector es ruido—. Se enviaba el
// PRIMERO que saliera, sin mirar su calidad, y el servidor lo rechazaba por
// "rostro no coincide": el 11 de septiembre N1-002 acumulo 0.036, 0.073, 0.25 y
// 0.29 en cuatro intentos seguidos, y 0.85 y 0.70 en los dos que si salieron.
// El rostro siempre fue el suyo; la LECTURA era basura.
//
// Varias lecturas de la misma cara se parecen mucho entre si; las basura no se
// parecen ni entre ellas. Asi que se toma la lectura que mas de acuerdo esta
// con las demas (la mediana en espiritu) y, si ni eso llega al minimo, NO se
// manda nada: se devuelve null y la pantalla pide reintentar. Eso es mejor que
// mandarla, porque una checada rechazada le queda al trabajador en su historial
// como si hubiera intentado suplantar a alguien.
//
// Nada de esto toca el umbral del servidor (0.60 rechaza / 0.70 acepta): se
// manda una lectura MEJOR, no un umbral mas flojo.
async function leerRostroConfiable(video, msg) {
  const lecturas = [];
  for (let i = 0; i < 10 && lecturas.length < 4; i++) {
    try {
      const r = await LuftFace.embed(video);
      // Se guarda la lectura COMPLETA (vector + calidad): el enrolamiento
      // necesita la calidad para mandarla al servidor, y antes se perdia aqui.
      if (r.quality >= MIN_CALIDAD_ROSTRO) {
        lecturas.push(r);
        // SALIDA TEMPRANA. Con DOS lecturas que concuerdan mucho entre si ya no
        // hace falta seguir leyendo: la tercera y la cuarta no aportan nada y en
        // un telefono cada lectura cuesta casi un segundo. Checar se sentia
        // lento por esto.
        //
        // Esto NO afloja el filtro. Las lecturas basura no concuerdan ni entre
        // ellas —el 11 de septiembre dieron 0.036, 0.073, 0.25 y 0.29—, asi que
        // nunca van a llegar a 0.80 y siguen pagando las 4 lecturas completas.
        // Solo se le deja de cobrar el tiempo a quien la camara ya vio bien.
        if (lecturas.length >= 2) {
          const a = lecturas[lecturas.length - 2].vec, b = lecturas[lecturas.length - 1].vec;
          if (LuftFace.cosine(a, b) >= ACUERDO_SUFICIENTE) return lecturas[lecturas.length - 1];
        }
      } else { msg.textContent = 'Acércate un poco: se te ve muy lejos…'; await new Promise((res) => setTimeout(res, 350)); }
    } catch (e) {
      msg.textContent = (e.message || 'no se ve tu cara') + '…';
      await new Promise((res) => setTimeout(res, 400));
    }
  }
  if (!lecturas.length) return null;
  if (lecturas.length === 1) {
    // Una sola lectura no se puede contrastar con nada. No se manda: es
    // justo el caso que producia los rechazos.
    msg.className = 'msg err';
    msg.textContent = 'No pude leer bien tu rostro. Ponte de frente, sin el sol atrás, y vuelve a intentar.';
    return null;
  }
  // Lectura mas "de acuerdo" con las demas.
  let mejor = null, mejorAcuerdo = -1;
  for (let i = 0; i < lecturas.length; i++) {
    let suma = 0;
    for (let j = 0; j < lecturas.length; j++) {
      if (i !== j) suma += LuftFace.cosine(lecturas[i].vec, lecturas[j].vec);
    }
    const acuerdo = suma / (lecturas.length - 1);
    if (acuerdo > mejorAcuerdo) { mejorAcuerdo = acuerdo; mejor = lecturas[i]; }
  }
  if (mejorAcuerdo < MIN_ACUERDO_LECTURAS) {
    msg.className = 'msg err';
    msg.textContent = 'La cámara no te está viendo bien (contraluz o movimiento). ' +
      'Date la vuelta para que la luz te dé en la cara y vuelve a intentar.';
    return null;
  }
  return mejor;
}

// ---------- selfie de auditoria (evidencia, en vivo) ----------
// La foto es evidencia para RH, gobernada por company_settings.audit_photo_enabled
// y cubierta por el aviso de privacidad que el trabajador ya acepto. Se toma del
// stream de camara (no de la galeria) para que sea del momento. Si la camara se
// niega o falla, NO se bloquea la checada: una falla de permiso no es falta.
let selfieStream = null;
function stopSelfieStream() {
  if (selfieStream) { try { selfieStream.getTracks().forEach((t) => t.stop()); } catch {} selfieStream = null; }
}

// Resuelve con un Blob JPEG, o null si el trabajador continua sin foto o la
// camara no esta disponible. `required` solo cambia el texto (nunca bloquea).
function captureSelfie(label, required) {
  return new Promise(async (resolve) => {
    if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)) return resolve(null);
    const video = $('selfie-video');
    const msg = $('selfie-msg'); msg.textContent = '';
    $('selfie-title').textContent = 'Foto de tu ' + (label || 'checada').toLowerCase();
    try {
      selfieStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user', width: { ideal: 640 }, height: { ideal: 640 } }, audio: false });
      video.srcObject = selfieStream;
    } catch (e) {
      // Sin camara o permiso denegado: seguimos sin foto.
      stopSelfieStream();
      return resolve(null);
    }
    show('selfie');

    const cleanup = () => { $('selfie-take').onclick = null; stopSelfieStream(); };
    $('selfie-take').onclick = () => {
      try {
        const c = $('selfie-canvas');
        const w = video.videoWidth || 480, h = video.videoHeight || 480;
        const side = Math.min(w, h);
        c.width = 480; c.height = 480;
        const ctx = c.getContext('2d');
        // Recorte cuadrado centrado, sin espejo en el archivo (el espejo es solo
        // para que el trabajador se vea natural en pantalla).
        ctx.drawImage(video, (w - side) / 2, (h - side) / 2, side, side, 0, 0, 480, 480);
        c.toBlob((blob) => { cleanup(); resolve(blob); }, 'image/jpeg', 0.7);
      } catch (e) { cleanup(); resolve(null); }
    };
  });
}

async function uploadSelfie(blob, opId) {
  const s = store.get('session'); const empId = s && s.employee && s.employee.id;
  if (!blob || !empId) return null;
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const path = empId + '/' + yyyy + '/' + mm + '/' + opId + '.jpg';
  try {
    const token = await accessToken();
    const res = await fetch(SUPABASE_URL + '/storage/v1/object/checadas-contexto/' + path, {
      method: 'POST',
      headers: { apikey: ANON_KEY, Authorization: 'Bearer ' + token, 'Content-Type': 'image/jpeg', 'x-upsert': 'false' },
      body: blob,
    });
    if (!res.ok) return null;
    return path;
  } catch { return null; }
}

// ---------- checada ----------
const PUNCH_LABEL = { in: 'Entrada', out: 'Salida', break_start: 'Inicio de comida', break_end: 'Regreso de comida' };

async function punch(type) {
  if (POL === null && navigator.onLine) await loadPolicy();
  busy(true, 'Obteniendo ubicación…');
  const dev = await ensureDevice();
  const loc = await getLocation();
  if (loc.status !== 'AUTORIZADA') {
    busy(false);
    const esIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) ||
      (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    let detalle;
    if (loc.status === 'DENEGADA') {
      // Guia CONCRETA por equipo: "actívala en configuración" no le dice a nadie
      // dónde. En iPhone el permiso vive en Localización, no en los ajustes de la
      // app, y por eso la gente no lo encontraba.
      detalle = esIOS
        ? 'La ubicación está bloqueada en este iPhone. Actívala así: Ajustes → ' +
          'Privacidad y seguridad → Localización (enciéndela) → «Sitios web de ' +
          'Safari» → «Al usar la app». Luego regresa aquí, recarga y toca checar. ' +
          'Conviene agregar la app a la pantalla de inicio (botón Compartir → ' +
          '«Agregar a inicio»): así es más estable y te pregunta el permiso al abrir.'
        : 'La ubicación está bloqueada para este sitio. Tócalo en el candado ' +
          'junto a la dirección → Ubicación → Permitir, recarga e intenta de nuevo.';
    } else {
      detalle = 'No se pudo obtener tu ubicación (señal débil o GPS ocupado). ' +
        'Ponte donde haya buena señal o cielo abierto e intenta de nuevo.';
    }
    return showResult('warn', 'Falta ubicación', detalle);
  }
  const opId = uuid();

  // Reto de "persona presente" con Face ID/Touch ID, verificado EN EL SERVIDOR:
  // el telefono firma un reto que emitio el servidor para esta operacion. Es una
  // capa sobre el control del servidor (firma del dispositivo + geocerca), no lo
  // sustituye: verification_method sigue siendo 'device_biometric'. Si falla o se
  // cancela, la checada NO se bloquea (una falla tecnica no es falta); el
  // servidor solo la registra como no verificada por passkey.
  let webauthn = null;
  if (store.get('bioGranted') && store.get('passkey')) {
    busy(true, 'Verificando con Face ID…');
    webauthn = await assertPasskey(opId);
  }

  // ---------- Reconocimiento facial (obligatorio para quien enroló) ----------
  // Si el trabajador autorizó y enroló su rostro, la IDENTIDAD la pone la cara:
  // se captura, se saca el vector aquí y el servidor lo compara 1:1 contra su
  // template. Con señal es obligatorio (no hay "saltar"). Sin señal aún no se
  // puede correr el modelo (las librerías van por CDN), así que se encola por el
  // método alterno y se sincroniza al reconectar; RH lo ve como offline_sync.
  if (FACE === null) await loadFaceStatus();
  let faceEmbedding = null, faceChallengeId = null, faceLiveness = null, facePad = null;
  let method = 'device_biometric';
  if (FACE && FACE.granted && FACE.enrolled) {
    busy(false);
    const cap = await capturarRostroChecada();
    if (cap && cap !== SIN_MOTOR) {
      faceEmbedding = Array.from(cap.vec);
      faceChallengeId = cap.challengeId; // null sin señal: el servidor no lo exige en offline_sync
      faceLiveness = cap.livenessPassed;
      facePad = cap.padScore;
      method = 'face';
    } else if (cap === SIN_MOTOR) {
      // Este telefono no puede correr el reconocimiento (equipo viejo, poca
      // memoria, navegador sin WebAssembly). Antes se quedaba atorado para
      // siempre: con el rostro enrolado la app se lo exigia en cada checada y
      // el equipo no podia darlo.
      //
      // Se sigue por el metodo alterno, que NO es un permiso gratis: la checada
      // viaja firmada con la llave de SU telefono aprobado, la geocerca se
      // aplica igual, y abajo se le pide la selfie de evidencia porque
      // faceEmbedding quedo vacio. RH la ve con foto y ubicacion.
      method = 'device_biometric';
    } else if (navigator.onLine) {
      // Con señal, el rostro es obligatorio: si no se reconoció, reintentar.
      return showResult('warn', 'Falta reconocer tu rostro',
        'Para checar, la app necesita ver tu cara y un pequeño movimiento. Acércate, con buena luz e intenta de nuevo.');
    }
    // Sin señal y sin poder leer el rostro (modelo aún no cacheado): se encola por
    // el método alterno y se sincroniza al reconectar.
  }

  // Selfie de auditoría: solo para quien NO checa por rostro (la cara ya es la
  // evidencia). Se sube antes, con el mismo opId como folio.
  let auditPhotoPath = null;
  if (!faceEmbedding && POL && POL.audit_photo_enabled && navigator.onLine) {
    busy(false);
    const blob = await captureSelfie(PUNCH_LABEL[type], POL.offsite_requires_photo);
    if (blob) { busy(true, 'Subiendo foto…'); auditPhotoPath = await uploadSelfie(blob, opId); }
  }

  busy(true, 'Registrando checada…');

  const deviceMs = Date.now();
  const payload = ['checada.v2', opId, dev.id, type, String(deviceMs),
    f6(loc.lat), f6(loc.lng), f1(loc.acc), '0'].join('|');
  const signature = await signPayload(dev.pair, payload);

  const body = {
    client_operation_id: opId, punch_type: type,
    device_time: new Date(deviceMs).toISOString(), device_id: dev.id,
    // La firma del dispositivo SIEMPRE viaja (respalda la geocerca). El método
    // dice quién puso la identidad: 'face' si reconoció el rostro, si no el alterno.
    verification_method: method, signature, signed_payload: payload,
    embedding: faceEmbedding || undefined,
    embedding_version: faceEmbedding ? ((FACE && FACE.embedding_version) || LuftFace.VERSION) : undefined,
    challenge_id: faceChallengeId || undefined,
    liveness_passed: faceLiveness == null ? undefined : faceLiveness,
    pad_score: facePad == null ? undefined : facePad,
    latitude: Number(f6(loc.lat)), longitude: Number(f6(loc.lng)),
    gps_accuracy_meters: Number(f1(loc.acc)), mock_location: false,
    integrity_level: 'amber', origin: 'online',
    audit_photo_path: auditPhotoPath || undefined,
    webauthn: webauthn || undefined,
  };

  const token = await accessToken();
  try {
    if (!navigator.onLine) throw new Error('offline');
    const r = await api('/functions/v1/punch_register', { body, auth: token });
    if (r.status === 401) { // sesion vencida: reintento con refresh
      const t2 = await accessToken();
      const r2 = await api('/functions/v1/punch_register', { body, auth: t2 });
      return handlePunchResponse(type, r2);
    }
    return handlePunchResponse(type, r);
  } catch (e) {
    await enqueue({ body, type, savedAt: deviceMs });
    busy(false);
    renderQueue();
    return showResult('warn', 'Guardada sin conexión',
      PUNCH_LABEL[type] + ' registrada a las ' + hhmm(deviceMs) +
      '. Se enviará automáticamente cuando haya internet. La hora se conserva.');
  } finally { busy(false); }
}

function handlePunchResponse(type, r) {
  busy(false);
  if (!r.ok || !r.data) {
    return showResult('err', 'No se registró', (r.data && r.data.error) || 'Error de servidor. Intenta de nuevo.');
  }
  const d = r.data;
  const st = d.status;
  // El servidor decide si el passkey fue valido (no el cliente).
  const fid = d.passkey_verified === true ? ' Verificado con Face ID.' : '';
  if (st === 'valid') return showResult('ok', PUNCH_LABEL[type] + ' registrada',
    (d.worksite ? 'En ' + d.worksite + '. ' : '') + 'Folio ' + (d.folio ?? '—') + '.' + fid);
  if (st === 'rejected') return showResult('err', PUNCH_LABEL[type] + ' rechazada',
    d.review_reason || 'No cumplió una validación (ubicación o firma).');
  return showResult('warn', PUNCH_LABEL[type] + ' a revisión',
    (d.review_reason || 'Queda pendiente de revisión de RH.') + ' Folio ' + (d.folio ?? '—') + '.');
}

// ---------- cola offline ----------
async function enqueue(item) { const q = (await idbGet('queue')) || []; q.push(item); await idbSet('queue', q); }
async function queue() { return (await idbGet('queue')) || []; }
let flushing = false;
async function flushQueue() {
  if (flushing || !navigator.onLine) return; // sin red no tiene caso; sin reentradas
  const q = await queue();
  if (!q.length) return;
  flushing = true;
  try {
    let token = await accessToken();
    const rest = [];
    for (const item of q) {
      // Al sincronizar diferido, la checada se marca como offline_sync para que RH
      // sepa que se capturo sin señal (la hora ya viaja en device_time firmado).
      const body = { ...item.body, origin: 'offline_sync' };
      try {
        let r = await api('/functions/v1/punch_register', { body, auth: token });
        if (r.status === 401) { // sesion vencida a media cola: refresca y reintenta una vez
          token = await accessToken();
          r = await api('/functions/v1/punch_register', { body, auth: token });
        }
        // ok, o duplicado ya registrado (el servidor es idempotente por
        // client_operation_id: 200 con duplicate:true, o 409) -> se saca de la cola.
        if (!r.ok && r.status !== 409) rest.push(item);
      } catch { rest.push(item); } // red se cayo de nuevo: se queda para el proximo intento
    }
    await idbSet('queue', rest);
    renderQueue();
  } finally { flushing = false; }
}
async function renderQueue() {
  const q = await queue();
  const el = $('queue');
  if (!q.length) { el.hidden = true; return; }
  el.hidden = false;
  el.textContent = q.length + ' checada(s) guardada(s) sin conexión. Se envían solas al reconectar.';
}

// ---------- UI ----------
function hhmm(ms) { const d = new Date(ms); return String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0'); }
function showResult(kind, title, detail) {
  $('result-badge').className = 'result-badge ' + kind;
  $('result-badge').textContent = kind === 'ok' ? '✓' : kind === 'warn' ? '!' : '✕';
  $('result-title').textContent = title;
  $('result-detail').textContent = detail;
  show('result');
}
function renderHome() {
  const s = store.get('session');
  const e = s && s.employee;
  $('hi').textContent = 'Hola' + (e && e.first_name ? ', ' + e.first_name : '');
  tickClock();
  updateChips();
  renderQueue();
  loadPolicy();
  show('home');
  // Si ya autorizó el biométrico pero aún no enrola su rostro, lo mandamos a
  // registrarlo (es requisito para checar con la cara). No bloquea si no aplica.
  loadFaceStatus().then(() => {
    if (FACE && FACE.granted && !FACE.enrolled && !$('home').hidden) renderEnrolar();
  });
}
function tickClock() { const d = new Date(); $('clock').textContent = hhmm(d.getTime()); }
async function updateChips() {
  const cap = deviceCapabilities();
  const net = navigator.onLine;
  setChip('chip-net', net ? 'ok' : 'warn', net ? 'En línea' : 'Sin conexión');
  setChip('chip-dev', 'ok', 'Registrado');
  // Ubicacion: estado del permiso si el navegador lo expone.
  if (navigator.permissions && navigator.permissions.query) {
    try {
      const p = await navigator.permissions.query({ name: 'geolocation' });
      const map = { granted: ['ok', 'Ubicación lista'], prompt: ['warn', 'Ubicación: pedirá permiso'], denied: ['err', 'Ubicación denegada'] };
      const [c, t] = map[p.state] || ['warn', 'Ubicación…']; setChip('chip-loc', c, t);
    } catch { setChip('chip-loc', 'warn', 'Ubicación…'); }
  } else setChip('chip-loc', cap.gps ? 'warn' : 'err', cap.gps ? 'Ubicación al checar' : 'Sin GPS');
}
function setChip(id, cls, txt) { const el = $(id); el.className = 'chip ' + cls; el.textContent = txt; }

function renderCaps() {
  const c = deviceCapabilities();
  const rows = [
    ['Sistema', c.os, 'y'], ['Navegador', c.browser, 'y'],
    ['Instalada (pantalla de inicio)', c.pwaInstalled ? 'Sí' : 'No', c.pwaInstalled ? 'y' : 'p'],
    ['Cámara', c.camera ? 'Disponible' : 'No', c.camera ? 'y' : 'n'],
    ['Ubicación', c.gps ? 'Disponible' : 'No', c.gps ? 'y' : 'n'],
    ['Face ID / passkey', c.passkeys ? 'Disponible' : 'No', c.passkeys ? 'y' : 'n'],
    ['Notificaciones', c.notifications ? 'Disponible' : 'No', c.notifications ? 'y' : 'p'],
    ['Funciona offline', c.offline ? 'Sí' : 'No', c.offline ? 'y' : 'n'],
    ['Ubicación en segundo plano', c.os === 'iOS' ? 'No en web (requiere app nativa)' : 'Limitado', 'n'],
    ['Conexión segura (HTTPS)', c.secureContext ? 'Sí' : 'No', c.secureContext ? 'y' : 'n'],
  ];
  $('cap-list').innerHTML = rows.map(([k, v, s]) =>
    `<li><span>${k}</span><b class="cap-${s}">${v}</b></li>`).join('');
}

// ---------- privacidad y acuerdos (perfil del trabajador) ----------
function fechaLarga(iso) {
  if (!iso) return '—';
  const d = new Date(iso); const p = (n) => String(n).padStart(2, '0');
  return p(d.getDate()) + '/' + p(d.getMonth() + 1) + '/' + d.getFullYear() + ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
}

function cardDoc(nombre, kind, doc, accV, accAt) {
  const alDia = accV != null && accV >= doc.version;
  const estado = alDia
    ? '<span class="etiqueta ok">Al día</span>'
    : '<span class="etiqueta aviso">Debes re-aceptar</span>';
  const legal = doc.legal_review_required ? ' · <em>borrador (revisión legal)</em>' : '';
  const linea = accV != null
    ? 'Aceptaste la v' + accV + ' el ' + fechaLarga(accAt) + '.'
    : 'Aún no lo aceptas.';
  return '<div class="priv-card">'
    + '<div class="priv-head"><strong>' + nombre + '</strong> ' + estado + '</div>'
    + '<div class="motivo small">Versión vigente: v' + doc.version + legal + '</div>'
    + '<div class="small">' + linea + '</div>'
    + '<button class="link" data-vertexto="' + kind + '">Ver texto</button>'
    + '<div class="doc" data-doc="' + kind + '" hidden>' + escapeHtml(doc.body) + '</div>'
    + '</div>';
}

function cardBio(doc, acc) {
  const decision = (acc && acc.biometric_decision) || (doc.decision || null);
  const estado = decision === 'granted' ? '<span class="etiqueta ok">Autorizado</span>'
    : decision === 'declined' ? '<span class="etiqueta">Método alternativo</span>'
    : '<span class="etiqueta aviso">Sin decisión</span>';
  const legal = doc.legal_review_required ? ' · <em>borrador (revisión legal)</em>' : '';
  const linea = decision === 'granted'
      ? 'Autorizaste el reconocimiento facial (v' + (acc ? acc.biometric_version : doc.version) + ') el ' + fechaLarga(acc && acc.accepted_at) + '.'
    : decision === 'declined'
      ? 'Elegiste método alternativo el ' + fechaLarga(acc && acc.accepted_at) + '.'
      : 'No has decidido. Es opcional y declinar no es sanción.';
  const boton = decision === 'granted'
    ? '<button class="link danger" data-bioaction="declined">Cambiar a método alternativo</button>'
    : '<button class="link" data-bioaction="granted">Autorizar reconocimiento facial</button>';
  return '<div class="priv-card">'
    + '<div class="priv-head"><strong>Reconocimiento facial (biométrico)</strong> ' + estado + '</div>'
    + '<div class="motivo small">Versión vigente: v' + doc.version + legal + '</div>'
    + '<div class="small">' + linea + '</div>'
    + '<button class="link" data-vertexto="biometric">Ver texto</button> · ' + boton
    + '<div class="doc" data-doc="biometric" hidden>' + escapeHtml(doc.body) + '</div>'
    + '</div>';
}

async function renderPrivacidad() {
  busy(true, 'Cargando…');
  try {
    const token = await accessToken();
    if (!AC) {
      const rs = await api('/rest/v1/rpc/agreements_status', { body: {}, auth: token });
      if (rs.ok && rs.data && !rs.data.error) AC = rs.data;
    }
    // Historial propio (RLS ya lo limita a las aceptaciones del trabajador).
    const r = await api(
      '/rest/v1/agreement_acceptances?select=accepted_at,labor_version,privacy_version,biometric_version,biometric_decision&order=accepted_at.desc&limit=50',
      { method: 'GET', auth: token });
    const filas = Array.isArray(r.data) ? r.data : [];
    const ult = (pred) => filas.find(pred) || null;
    const aLabor = ult((f) => f.labor_version != null);
    const aPriv = ult((f) => f.privacy_version != null);
    const aBio = ult((f) => f.biometric_version != null);

    const cards = [];
    if (AC && AC.labor) cards.push(cardDoc('Acuerdo de asistencia', 'labor', AC.labor, aLabor && aLabor.labor_version, aLabor && aLabor.accepted_at));
    if (AC && AC.privacy) cards.push(cardDoc('Aviso de privacidad', 'privacy', AC.privacy, aPriv && aPriv.privacy_version, aPriv && aPriv.accepted_at));
    if (AC && AC.biometric) cards.push(cardBio(AC.biometric, aBio));
    $('priv-list').innerHTML = cards.length ? cards.join('') : '<p class="muted small">No hay documentos configurados.</p>';
    show('privacidad');
  } finally { busy(false); }
}

// ---------- arranque ----------
function bindUI() {
  $('code').addEventListener('input', (e) => {
    e.target.value = e.target.value.replace(/\D/g, '').slice(0, 6);
    $('enroll-btn').disabled = e.target.value.length !== 6;
  });
  $('enroll-btn').addEventListener('click', async () => {
    const r = await enroll($('code').value);
    const msg = $('enroll-msg');
    if (r.ok) { msg.textContent = ''; gateAgreements(); }
    else { msg.className = 'msg err'; msg.textContent = r.msg; }
  });
  document.querySelectorAll('#ac-checks input').forEach((c) => c.addEventListener('change', () => {
    $('ac-btn').disabled = !Object.values(acChecks()).every(Boolean);
  }));
  $('ac-btn').addEventListener('click', acceptAgreement);
  document.querySelectorAll('#bio-checks input').forEach((c) => c.addEventListener('change', () => {
    $('bio-btn').disabled = !Object.values(bioChecks()).every(Boolean);
  }));
  $('bio-btn').addEventListener('click', () => decideBiometric('granted'));
  $('bio-alt').addEventListener('click', () => decideBiometric('declined'));
  document.querySelectorAll('[data-punch]').forEach((b) =>
    b.addEventListener('click', () => punch(b.dataset.punch)));
  $('result-ok').addEventListener('click', renderHome);
  $('signout').addEventListener('click', () => { store.del('session'); location.reload(); });
  $('priv-link').addEventListener('click', renderPrivacidad);
  $('priv-back').addEventListener('click', renderHome);
  $('priv-list').addEventListener('click', (e) => {
    const t = e.target;
    const ver = t.getAttribute && t.getAttribute('data-vertexto');
    if (ver) {
      const doc = document.querySelector('[data-doc="' + ver + '"]');
      if (doc) { doc.hidden = !doc.hidden; t.textContent = doc.hidden ? 'Ver texto' : 'Ocultar texto'; }
      return;
    }
    const bio = t.getAttribute && t.getAttribute('data-bioaction');
    if (bio === 'granted') { renderBiometrico(); }
    else if (bio === 'declined') {
      if (confirm('¿Cambiar a método alternativo? Se registrará tu decisión. No es sanción.')) decideBiometric('declined');
    }
  });
  $('perm-link').addEventListener('click', () => { renderCaps(); show('permisos'); });
  $('perm-link-enroll').addEventListener('click', () => { renderCaps(); show('permisos'); });
  $('perm-back').addEventListener('click', () => (store.get('session') ? renderHome() : show('enroll')));
  $('banner-ok').addEventListener('click', () => { store.set('bannerAck', APP_VERSION); $('banner').hidden = true; });
  window.addEventListener('online', () => { updateChips(); flushQueue(); });
  window.addEventListener('offline', updateChips);
  // El evento 'online' no siempre dispara en iOS. Reforzamos la sincronia al
  // volver la app a primer plano y con un latido periodico: flushQueue() sale
  // solo si hay red y algo en cola, asi que es barato.
  document.addEventListener('visibilitychange', () => { if (!document.hidden) { updateChips(); flushQueue(); } });
  setInterval(() => flushQueue(), 60000);
  setInterval(tickClock, 15000);
}

function boot() {
  bindUI();
  if (store.get('bannerAck') !== APP_VERSION) $('banner').hidden = false;

  // La RED NUNCA decide la primera pantalla. Antes, con sesion, el arranque
  // esperaba a gateAgreements() y si la red colgaba la app se quedaba atorada en
  // "Cargando" para siempre (bug de campo real). Ahora pintamos YA una pantalla
  // usable —Home si hay sesion, Registro si no— y las revisiones de red corren
  // en segundo plano: si resulta que falta aceptar un acuerdo, gateAgreements()
  // cambia a esa pantalla despues, sin bloquear.
  if (store.get('session')) { renderHome(); gateAgreements(); flushQueue(); }
  else show('enroll');

  // Registro/actualizacion del service worker: en segundo plano, jamas bloquea.
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js')
      .then((reg) => { try { reg.update(); } catch {} })
      .catch(() => {});
  }

  // Red de seguridad: si por cualquier razon seguimos en "Cargando" a los 3 s,
  // forzamos una pantalla usable. Nunca se puede quedar colgada la entrada.
  setTimeout(() => {
    const l = $('loading');
    if (l && !l.hidden) { store.get('session') ? renderHome() : show('enroll'); }
  }, 3000);
}
boot();
