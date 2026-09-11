/* Service worker LUFT: cachea el "app shell" para que la app abra AL INSTANTE,
   con o sin internet. Las llamadas al backend NUNCA se cachean (van a la red). */
const CACHE = 'luft-shell-v17';
const SHELL = [
  './', './index.html', './styles.css', './app.js', './face.js', './manifest.webmanifest',
  './icon-192.png', './icon-512.png', './icon-maskable-512.png',
  // Tipografias servidas por este mismo dominio (antes venian de Google). Van en
  // el shell para que sin señal la app se vea igual. Solo el subconjunto latino:
  // cubre á é í ó ú ñ, que es todo lo que hace falta en español.
  '../fonts/fonts.css',
  '../fonts/archivo-400-latin.woff2',
  '../fonts/archivo-500-latin.woff2',
  '../fonts/archivo-600-latin.woff2',
  '../fonts/archivo-700-latin.woff2',
  '../fonts/cormorant-500-latin.woff2',
  '../fonts/cormorant-600-latin.woff2',
  '../fonts/cormorant-600-italic-latin.woff2',
  // Reconocimiento facial. Sin estos archivos la checada NO funciona sin señal:
  // el instructivo promete que funciona en obra, y esto es lo que lo cumple.
  // (El modelo facenet.tflite viene de Supabase y se guarda solo en IndexedDB;
  //  ver face.js. Por eso la PRIMERA carga sí necesita señal.)
  './vendor/tf.min.js',
  './vendor/blazeface.min.js',
  './vendor/tf-tflite.min.js',
  './vendor/blazeface/model.json',
  './vendor/blazeface/group1-shard1of1.bin',
  './vendor/wasm/tflite_web_api_cc.js',
  './vendor/wasm/tflite_web_api_cc.wasm',
  './vendor/wasm/tflite_web_api_cc_simd.js',
  './vendor/wasm/tflite_web_api_cc_simd.wasm',
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
  // El APK de Android (~90 MB) NO se cachea: se descarga una vez para instalar.
  if (url.pathname.endsWith('.apk')) return;
  // App shell: STALE-WHILE-REVALIDATE. Se responde YA con lo cacheado (arranque
  // inmediato aunque la señal sea debil o nula, que es el caso de obra) y, si hay
  // red, se refresca la copia en segundo plano para que la proxima apertura traiga
  // lo nuevo (politica o pantalla). Nunca se espera a la red para pintar la app.
  e.respondWith(
    caches.open(CACHE).then(async (cache) => {
      // index.html pide los archivos con ?b=NN (app.js?b=14) y el shell se guarda
      // SIN query, asi que el match exacto falla. Si no hay exacto, se busca
      // ignorando la query: si no, sin señal no se encontraria nada del shell.
      const hit = (await cache.match(e.request)) ||
                  (await cache.match(e.request, { ignoreSearch: true }));
      const fresh = fetch(e.request).then((res) => {
        if (res && res.ok) cache.put(e.request, res.clone());
        return res;
      }).catch(() => null);
      if (hit) return hit;
      const res = await fresh;
      if (res) return res;
      // Sin cache y sin red: SOLO una navegacion cae al index, para que la PWA
      // abra igual. Lo demas debe FALLAR: devolverle el index a app.js o a
      // tf.min.js entrega HTML donde se espera JavaScript, el script no parsea
      // y la app queda EN BLANCO. Mejor que falle esa peticion sola.
      if (e.request.mode === 'navigate') return cache.match('./index.html');
      return Response.error();
    }),
  );
});
