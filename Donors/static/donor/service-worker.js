const CACHE_NAME = 'bloodgrp-cache-v1';
const urlsToCache = [
    '/',
    '/static/css/styles.css',
    '/static/js/main.js',
    '/static/images/blood_donate.jpeg',
    '/static/images/blood_donate2.jpeg',
    '/static/images/logo.png',
    // Add any other files you want to cache here
];

// service-worker.js

// Install event
self.addEventListener('install', (event) => {
  console.log('Service Worker: Install event triggered');
  event.waitUntil(
      caches.open('my-cache').then((cache) => {
          console.log('Opened cache');
          return cache.addAll([
              '/',
              '/static/css/styles.css',
              '/static/donor/service-worker.js',
          ]).catch(error => {
              console.error('Failed to cache resources:', error);
          });
      })
  );
});


  
  // Activate event
  self.addEventListener('activate', (event) => {
    console.log('Service Worker activated');
    // Clean up old caches if needed
    event.waitUntil(
      caches.keys().then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== 'my-cache') {
              return caches.delete(cacheName);
            }
          })
        );
      })
    );
  });
  
  // Fetch event (to serve cached content)
  self.addEventListener('fetch', (event) => {
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        return cachedResponse || fetch(event.request);
      })
    );
  });  
