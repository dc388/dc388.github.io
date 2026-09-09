/* LuftFace — reconocimiento facial en el navegador con el MISMO modelo que Android.
 *
 *   FaceNet 128-d (facenet.tflite, version 'facenet-128d-v1') corrido con
 *   tfjs-tflite (WASM). El rostro NUNCA sale del telefono: aqui se convierte en
 *   un vector de 128 numeros y solo ese vector viaja (ADR-0001). La comparacion
 *   1:1 contra el template del empleado ocurre en el servidor.
 *
 *   Preprocesamiento identico a FaceNetCapture.kt (Android): detectar la cara
 *   mas grande, recortar con 20% de margen, 160x160, prewhiten (estandarizacion
 *   por imagen), FaceNet, L2-normalizar. Asi los vectores viven en el MISMO
 *   espacio y un rostro enrolado en web se verifica en Android y viceversa.
 *
 *   El modelo (23 MB) se cachea en IndexedDB tras la primera carga, para que
 *   funcione OFFLINE en obra (una vez descargado con señal).
 */
(function (global) {
  'use strict';

  const MODEL_URL = 'https://lsduggmuwbvrudpfcgtm.supabase.co/storage/v1/object/public/app/facenet.tflite';
  const MODEL_BYTES = 23705216;
  const VERSION = 'facenet-128d-v1';
  const IMG = 160, MARGIN = 0.20;
  // Todo local (mismo origen) para que funcione OFFLINE: el service worker los
  // cachea en la primera carga con señal, y de ahí en adelante cargan sin red.
  // WASM y modelo Blazeface van por URL ABSOLUTA (tf-tflite/tf.io no resuelven
  // bien las relativas); las librerías por <script> sí resuelven contra la página.
  const _base = (document && document.baseURI) || location.href;
  const WASM_PATH = new URL('vendor/wasm/', _base).href;
  const BLAZEFACE_MODEL = new URL('vendor/blazeface/model.json', _base).href;
  const LIBS = [
    'vendor/tf.min.js',
    'vendor/blazeface.min.js',
    'vendor/tf-tflite.min.js',
  ];

  let _detector = null, _model = null, _loading = null;

  function loadScript(src) {
    return new Promise((res, rej) => {
      const s = document.createElement('script');
      s.src = src; s.onload = () => res(); s.onerror = () => rej(new Error('no cargó ' + src));
      document.head.appendChild(s);
    });
  }

  // --- caché del modelo en IndexedDB (para offline) ---
  function mdb() {
    return new Promise((res, rej) => {
      const r = indexedDB.open('luft-face', 1);
      r.onupgradeneeded = () => r.result.createObjectStore('kv');
      r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
    });
  }
  async function mGet(k) { const db = await mdb(); return new Promise((res, rej) => { const t = db.transaction('kv').objectStore('kv').get(k); t.onsuccess = () => res(t.result); t.onerror = () => rej(t.error); }); }
  async function mSet(k, v) { const db = await mdb(); return new Promise((res, rej) => { const t = db.transaction('kv', 'readwrite').objectStore('kv').put(v, k); t.onsuccess = () => res(); t.onerror = () => rej(t.error); }); }

  async function modelBytes() {
    // 1) caché local (offline). 2) red, y se cachea.
    try {
      const cached = await mGet('facenet-' + VERSION);
      if (cached && cached.byteLength === MODEL_BYTES) return cached;
    } catch (e) {}
    const buf = await (await fetch(MODEL_URL)).arrayBuffer();
    if (buf.byteLength !== MODEL_BYTES) throw new Error('descarga del modelo incompleta');
    try { await mSet('facenet-' + VERSION, buf); } catch (e) {}
    return buf;
  }

  // Prepara librerías + detector + modelo. Idempotente. Devuelve true si listo.
  async function ready() {
    if (_model && _detector) return true;
    if (_loading) return _loading;
    _loading = (async () => {
      for (const lib of LIBS) { if (!hasLib(lib)) await loadScript(lib); }
      await global.tf.ready();
      global.tflite.setWasmPath(WASM_PATH);
      if (!_detector) _detector = await global.blazeface.load({ modelUrl: BLAZEFACE_MODEL });
      if (!_model) _model = await global.tflite.loadTFLiteModel(await modelBytes());
      return true;
    })();
    try { return await _loading; } catch (e) { _loading = null; throw e; }
  }

  function hasLib(src) {
    if (src.includes('tf-tflite')) return !!global.tflite;
    if (src.includes('blazeface')) return !!global.blazeface;
    if (src.includes('tf.min')) return !!global.tf;
    return false;
  }

  // Saca el embedding L2-normalizado (128-d) del rostro más grande del video.
  // Lanza FaceNotFound si no hay cara clara. { vec: Float32Array, quality: 0..1 }
  async function embed(video) {
    await ready();
    const tf = global.tf;
    const faces = await _detector.estimateFaces(video, false);
    if (!faces.length) throw new FaceNotFound('no se ve una cara clara; acércate y evita el contraluz');
    faces.sort((a, b) =>
      ((b.bottomRight[0] - b.topLeft[0]) * (b.bottomRight[1] - b.topLeft[1])) -
      ((a.bottomRight[0] - a.topLeft[0]) * (a.bottomRight[1] - a.topLeft[1])));
    const f = faces[0];
    let x1 = f.topLeft[0], y1 = f.topLeft[1], x2 = f.bottomRight[0], y2 = f.bottomRight[1];
    const mw = (x2 - x1) * MARGIN, mh = (y2 - y1) * MARGIN;
    x1 = Math.max(0, x1 - mw); y1 = Math.max(0, y1 - mh);
    x2 = Math.min(video.videoWidth, x2 + mw); y2 = Math.min(video.videoHeight, y2 + mh);

    const c = document.createElement('canvas'); c.width = IMG; c.height = IMG;
    const ctx = c.getContext('2d');
    ctx.drawImage(video, x1, y1, x2 - x1, y2 - y1, 0, 0, IMG, IMG);
    const px = ctx.getImageData(0, 0, IMG, IMG).data;
    const n = IMG * IMG;

    // prewhiten: media/desv estándar sobre todos los canales RGB (igual Android).
    let sum = 0, sumSq = 0;
    const r = new Float32Array(n), g = new Float32Array(n), b = new Float32Array(n);
    for (let i = 0; i < n; i++) {
      const rr = px[i * 4], gg = px[i * 4 + 1], bb = px[i * 4 + 2];
      r[i] = rr; g[i] = gg; b[i] = bb;
      sum += rr + gg + bb; sumSq += rr * rr + gg * gg + bb * bb;
    }
    const count = n * 3, mean = sum / count;
    const std = Math.sqrt(Math.max(sumSq / count - mean * mean, 0));
    const stdAdj = Math.max(std, 1 / Math.sqrt(count));
    const buf = new Float32Array(n * 3);
    for (let i = 0; i < n; i++) {
      buf[i * 3] = (r[i] - mean) / stdAdj;
      buf[i * 3 + 1] = (g[i] - mean) / stdAdj;
      buf[i * 3 + 2] = (b[i] - mean) / stdAdj;
    }
    const input = tf.tensor(buf, [1, IMG, IMG, 3]);
    const o = _model.predict(input);
    const raw = await o.data();
    input.dispose(); o.dispose();

    let s = 0; for (const x of raw) s += x * x; const norm = Math.sqrt(s) || 1;
    const vec = new Float32Array(raw.length); for (let i = 0; i < raw.length; i++) vec[i] = raw[i] / norm;
    const quality = ((x2 - x1) * (y2 - y1)) / (video.videoWidth * video.videoHeight);
    return { vec, quality: Math.max(0, Math.min(1, quality)) };
  }

  function FaceNotFound(msg) { this.name = 'FaceNotFound'; this.message = msg; }
  FaceNotFound.prototype = Object.create(Error.prototype);

  // ¿El navegador tiene lo mínimo para reconocimiento facial?
  function supported() {
    return !!(global.WebAssembly && global.indexedDB && navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  }

  // Devuelve el recuadro de la cara más grande {x,y,w,h} o null. Para el reto de
  // vida (medir movimiento): una foto estática no cambia de tamaño/posición.
  async function detectBox(video) {
    await ready();
    const faces = await _detector.estimateFaces(video, false);
    if (!faces.length) return null;
    faces.sort((a, b) =>
      ((b.bottomRight[0] - b.topLeft[0]) * (b.bottomRight[1] - b.topLeft[1])) -
      ((a.bottomRight[0] - a.topLeft[0]) * (a.bottomRight[1] - a.topLeft[1])));
    const f = faces[0];
    return { x: f.topLeft[0], y: f.topLeft[1], w: f.bottomRight[0] - f.topLeft[0], h: f.bottomRight[1] - f.topLeft[1] };
  }

  global.LuftFace = { ready, embed, detectBox, supported, VERSION, FaceNotFound, cosine };

  function cosine(a, b) { let d = 0; for (let i = 0; i < a.length; i++) d += a[i] * b[i]; return d; }
})(window);
