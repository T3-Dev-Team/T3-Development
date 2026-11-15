// Public issue map with filters and grouped markers. UC-005, F-006, NF-02, NF-07.
// Expects a list "reports" from the view; each item: id, lat, lng, category, status (code, e.g. in_repair), status_label (e.g. In Repair), created (YYYY-MM-DD),
// address, description, url (optional). Never include the reporter's name or email (NF-07).
window.initIssuesMap = async function () {
  const $ = (id) => document.getElementById(id);
  try {
    const reports = JSON.parse($("reports-data").textContent);
    const d = $("issues-map").dataset;
    const center = { lat: Number(d.centerLat) || 45.815, lng: Number(d.centerLng) || 15.982 }; // default map centre
    const { Map, InfoWindow } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const map = new Map($("issues-map"), { center, zoom: 13, mapId: "DEMO_MAP_ID", streetViewControl: false, mapTypeControl: false });
    const info = new InfoWindow();
    const clusterer = new markerClusterer.MarkerClusterer({ map });

    const popup = (r) => {
      const box = document.createElement("div");
      const add = (tag, text) => { const e = document.createElement(tag); e.textContent = text; box.appendChild(e); return e; };
      add("strong", r.category);
      add("p", (r.status_label || r.status) + (r.created ? " · " + r.created : ""));
      if (r.address) add("p", r.address);
      if (r.description) add("p", r.description);
      if (r.url) { const a = add("a", "View details"); a.href = r.url; }
      return box;
    };

    const items = reports.map((r) => {
      const marker = new AdvancedMarkerElement({ position: { lat: Number(r.lat), lng: Number(r.lng) }, title: r.category });
      marker.addListener("click", () => { info.setContent(popup(r)); info.open({ map, anchor: marker }); });
      return { r, marker };
    });

    const fill = (id, pairs) => pairs.forEach(([value, label]) => { const o = document.createElement("option"); o.value = value; o.textContent = label; $(id).appendChild(o); });
    fill("f-category", [...new Set(reports.map((r) => r.category))].sort().map((c) => [c, c]));
    const statuses = {};
    reports.forEach((r) => { statuses[r.status] = r.status_label || r.status; });
    fill("f-status", Object.entries(statuses).sort((a, b) => a[1].localeCompare(b[1])));

    function apply() {
      const c = $("f-category").value, s = $("f-status").value, from = $("f-from").value, to = $("f-to").value;
      const shown = items.filter(({ r }) => {
        const day = String(r.created || "").slice(0, 10);
        return (!c || r.category === c) && (!s || r.status === s) && (!from || day >= from) && (!to || day <= to);
      });
      clusterer.clearMarkers();
      clusterer.addMarkers(shown.map((i) => i.marker));
      $("map-count").textContent = shown.length + " of " + items.length + " reports shown";
      $("map-empty").hidden = shown.length > 0;
    }
    ["f-category", "f-status", "f-from", "f-to"].forEach((id) => $(id).addEventListener("change", apply));
    $("f-reset").addEventListener("click", () => { $("filters").reset(); apply(); });
    apply();
  } catch (err) {
    console.error(err);
    $("map-error").hidden = false;
  }
};
