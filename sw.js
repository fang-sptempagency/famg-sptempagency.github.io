//2019.8.10 REFERENCE from
//https://jam25.jp/programing/about-pwa/#outline__6

var CACHE_DYNAMIC_VERSION = 'dynamic-v1';

self.addEventListener('fetch', function(event) {
    console.log('[Service Worker] Fetching something ...');
    event.respondWith(
        caches.match(event.request)
        .then(function(response) {
            if (response) {
                return response;
            } else {
                return fetch(event.request)
                    .then(function(res) {
                    return caches.open(CACHE_DYNAMIC_VERSION)
                        .then(function(cache) {
                        cache.put(event.request.url, res.clone());
                        return res;
                    })
                })
                    .catch(function() {
                });
            }
        })
    );
});