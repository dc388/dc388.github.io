/* Service worker LUFT: cachea el "app shell" para que la app abra AL INSTANTE,
   con o sin internet. Las llamadas al backend NUNCA se cachean (van a la red). */
const CACHE = 'luft-shell-v28';
const SHELL = [
  './', './index.html', './styles.css', './app.js', './face.js', './manifest.webmanifest',
  './icon-192.png', './icon-512.png',
  // Tipografias: antes venian de Google en cada carga. Ahora las sirve este
  // mismo dominio, asi que la app ya no le pide NADA a terceros. Solo el
  // subconjunto latino, que cubre á é í ó ú ñ.
  '../fonts/fonts.css',
  '../fonts/archivo-400-latin.woff2',
  '../fonts/archivo-500-latin.woff2',
  '../fonts/archivo-600-latin.woff2',
  '../fonts/archivo-700-latin.woff2',
  '../fonts/cormorant-500-latin.woff2',
  '../fonts/cormorant-600-latin.woff2',
  '../fonts/cormorant-600-italic-latin.woff2',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) =>
    Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  // Backend: siempre red (no cachear datos de asistencia ni de sesion).
  if (url.origin.includes('supabase.co') || e.request.method !== 'GET') return;
  if (url.origin !== self.location.origin) return;
  // El APK de Android (~78 MB) NO se cachea: se descarga una vez para instalar.
  if (url.pathname.endsWith('.apk')) return;
  // El modelo de rostro (23 MB) tampoco: face.js ya lo guarda en IndexedDB, que
  // es SU camino para funcionar offline. Cachearlo aqui ademas lo duplicaba a 46
  // MB y, en iPhone, el cache.put de esa respuesta se topa con la cuota de
  // Safari. Lo unico que aportaba era una forma mas de atorar la descarga.
  if (url.pathname.endsWith('.tflite')) return;
  // App shell: STALE-WHILE-REVALIDATE. Se responde YA con lo cacheado (arranque
  // inmediato aunque la señal sea debil o nula, que es el caso de obra) y, si hay
  // red, se refresca la copia en segundo plano para que la proxima apertura traiga
  // lo nuevo (politica o pantalla). Nunca se espera a la red para pintar la app.
  e.respondWith(
    caches.open(CACHE).then(async (cache) => {
      // index.html pide los archivos con ?b=NN (app.js?b=26, styles.css?b=19) y
      // el shell los guarda SIN query, asi que el match EXACTO nunca acierta.
      // Sin este segundo intento que ignora la query, cada subida de ?b= dejaba
      // a todo el mundo dependiendo de la red, y con señal debil se caia al
      // index: el navegador recibia HTML donde esperaba JavaScript, el script no
      // parseaba y la app quedaba muerta. Eso es lo que se vio en la nave.
      const hit = (await cache.match(e.request)) ||
                  (await cache.match(e.request, { ignoreSearch: true }));
      const fresh = fetch(e.request).then((res) => {
        if (res && res.ok) cache.put(e.request, res.clone());
        return res;
      }).catch(() => null);
      // Con cache: responde ya y refresca atras.
      if (hit) return hit;
      const res = await fresh;
      if (res) return res;
      // Sin cache y sin red: SOLO una navegacion cae al index, para que la PWA
      // abra igual. Para todo lo demas es mejor fallar: devolverle el index a
      // app.js o a un .wasm es lo que dejaba la pantalla en blanco sin decir
      // por que. Un recurso que falla si se nota y se puede reintentar.
      if (e.request.mode === 'navigate') return cache.match('./index.html');
      return Response.error();
    }),
  );
});
