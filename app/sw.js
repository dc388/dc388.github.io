/* Service worker LUFT: cachea el "app shell" para que la app abra AL INSTANTE,
   con o sin internet. Las llamadas al backend NUNCA se cachean (van a la red). */
const CACHE = 'luft-shell-v18';
const SHELL = [
  './', './index.html', './styles.css', './app.js', './manifest.webmanifest',
  './icon-192.png', './icon-512.png',
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
  // App shell: STALE-WHILE-REVALIDATE. Se responde YA con lo cacheado (arranque
  // inmediato aunque la señal sea debil o nula, que es el caso de obra) y, si hay
  // red, se refresca la copia en segundo plano para que la proxima apertura traiga
  // lo nuevo (politica o pantalla). Nunca se espera a la red para pintar la app.
  e.respondWith(
    caches.open(CACHE).then((cache) =>
      cache.match(e.request).then((hit) => {
        const fresh = fetch(e.request).then((res) => {
          if (res && res.ok) cache.put(e.request, res.clone());
          return res;
        }).catch(() => null);
        // Con cache: responde ya y refresca atras. Sin cache: espera la red y, si
        // no hay, cae al index para que la PWA abra igual.
        return hit || fresh.then((res) => res || cache.match('./index.html'));
      })),
  );
});
