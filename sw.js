const CACHE_NAME = 'avai-prep-v8';
const STATIC_ASSETS = [
  './',
  './index.html',
  './icon.svg',
  './manifest.json',
  './calculator.html',
  './about.html',
  './privacy.html',
  './style.css',
  './script.js',
  './data/physics_questions.js',
  './data/physics_questions.json',
  './data/syllabus.js'
];

// Cache core assets on install
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(STATIC_ASSETS).catch(err => {
        console.warn('PWA Asset caching notice:', err);
      });
    })
  );
  self.skipWaiting();
});

// Clean up old caches on activate
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Network first with cache fallback strategy
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  // Ignore chrome-extension or external analytics schemes
  if (!event.request.url.startsWith('http')) return;

  event.respondWith(
    fetch(event.request)
      .then(networkRes => {
        if (networkRes && networkRes.status === 200) {
          const resClone = networkRes.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, resClone));
        }
        return networkRes;
      })
      .catch(() => caches.match(event.request).then(cached => cached || caches.match('./index.html')))
  );
});