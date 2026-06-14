const addr = window.STATIC_ADDRESS | "";

const CATALOGUE_ASSETS = "catalogue-assets";

// Paths are relative to this service worker's scope (the /static/js/ folder),
// so step up one level to reach /static/
const assets = [
  "../css/style.css",
  "../css/bootstrap.min.css",
  "bootstrap.bundle.min.js",
  "app.js",
  "../images/favicon.png",
  "../icons/icon-128x128.png",
  "../icons/icon-192x192.png",
  "../icons/icon-384x384.png",
  "../icons/icon-512x512.png",
];

self.addEventListener("install", (installEvt) => {
  installEvt.waitUntil(
    caches
      .open(CATALOGUE_ASSETS)
      .then((cache) => cache.addAll(assets))
      .then(() => self.skipWaiting())
      .catch((e) => console.log(e)),
  );
});

self.addEventListener("activate", function (evt) {
  evt.waitUntil(
    caches
      .keys()
      .then((keyList) =>
        Promise.all(
          keyList.map((key) => {
            // Delete OLD caches, keep the current one
            if (key !== CATALOGUE_ASSETS) {
              console.log("Removed old cache:", key);
              return caches.delete(key);
            }
          }),
        ),
      )
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", function (evt) {
  evt.respondWith(
    fetch(evt.request).catch(() =>
      caches.open(CATALOGUE_ASSETS).then((cache) => cache.match(evt.request)),
    ),
  );
});
