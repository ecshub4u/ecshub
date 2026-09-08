const CACHE_NAME = "ecshub-shell-v3";
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

  const url = new URL(e.request.url);
  const isNavigation = e.request.mode === "navigate" || e.request.destination === "document";
  const isAppShell = isNavigation || url.pathname.endsWith("/manifest.json");

  if (isAppShell) {
    // Network-first for the app shell itself. update.py + pushing a new
    // index.html doesn't touch this file, so relying on "a new SW
    // version was published" to refresh the shell means routine content
    // updates would never reach students who already have it cached.
    // Always try the network first so new features/content/files show
    // up the moment someone opens the app with internet; the cache is
    // only a fallback for offline opens.
    e.respondWith(
      fetch(e.request)
        .then(r => {
          if (r && r.ok) {
            const copy = r.clone();
            caches.open(CACHE_NAME).then(c => c.put(e.request, copy));
          }
          return r;
        })
        .catch(() => caches.match(e.request).then(cached => cached || caches.match("./index.html")))
    );
    return;
  }

  // Study material and other assets: cache-first. Once a file's been
  // opened once, it works offline and doesn't get re-downloaded every
  // visit. A missing/offline file fails as itself (504) rather than
  // silently returning index.html — see the note in openFile's error
  // handling on the page for why that matters.
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
        .catch(() => new Response("", { status: 504, statusText: "Offline and not cached" }));
    })
  );
});
