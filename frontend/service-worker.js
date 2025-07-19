const CACHE_NAME = 'smartstock-cache-v1';
const FILES_TO_CACHE = [
  '/frontend/html/dashboard.html',
  '/frontend/lang/en.json',
  '/frontend/lang/fr.json',
  '/frontend/lang/rw.json',
  'https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap',
  'https://unpkg.com/feather-icons'
];

// Cache important files on install
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(FILES_TO_CACHE))
  );
  self.skipWaiting();
});

// Remove old caches on activate
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(key => key !== CACHE_NAME && caches.delete(key)))
    )
  );
  self.clients.claim();
});

// Intercept fetch requests
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(cached =>
      cached || fetch(event.request).catch(() => {
        if (event.request.destination === 'document') {
          return caches.match('/frontend/html/dashboard.html');
        }
      })
    )
  );
});
