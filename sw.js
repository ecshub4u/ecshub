const CACHE_NAME = "ecshub-shell-v2";
const APP_SHELL = ["./", "./index.html", "./manifest.json"];

self.addEventListener("install", e =>
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(APP_SHELL)).then(() => self.skipWaiting()))
);

self.addEventListener("activate", e =>
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  )
);

self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;

  // Only an actual page load (the app shell itself) should fall back to
  // index.html when offline. Study material (PDFs, images, txt, etc.)
  // must fail as itself when it isn't cached and there's no network —
  // silently swapping in index.html made offline file-opens show the
  // site's own HTML source instead of a clear "you're offline" state.
  const isNavigation = e.request.mode === "navigate" || e.request.destination === "document";

  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request)
        .then(r => {
          if (r && r.ok) {
            const copy = r.clone();
            caches.open(CACHE_NAME).then(c => c.put(e.request, copy));
          }
          return r;
        })
        .catch(() => {
          if (isNavigation) return caches.match("./index.html");
          return new Response("", { status: 504, statusText: "Offline and not cached" });
        });
    })
  );
});
