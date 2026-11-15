// Report form: choose a location by GPS, typed address (with suggestions) or a pin on the map.
// Fills the hidden fields latitude, longitude and address. UC-002, F-003, F-004, NF-09, NF-10.
(function () {
  const $ = (id) => document.getElementById(id);
  const form = $("report-form");
  const CENTER = { lat: Number(form.dataset.centerLat) || 45.815, lng: Number(form.dataset.centerLng) || 15.982 }; // default map centre: set map_center_lat/lng in the view, or change here
  let map, marker, geocoder;

  const say = (msg, isError) => { const s = $("location-status"); s.textContent = msg; s.classList.toggle("error", !!isError); };
  const toLiteral = (p) => (typeof p.lat === "function" ? { lat: p.lat(), lng: p.lng() } : p);

  function setLocation(point, address) {
    const pos = toLiteral(point);
    $("latitude").value = pos.lat.toFixed(6);
    $("longitude").value = pos.lng.toFixed(6);
    marker.position = pos;
    marker.map = map;
    map.panTo(pos);
    if (address) { $("address").value = address; say("Location: " + address); return; }
    geocoder.geocode({ location: pos }).then((res) => {
      const a = res.results && res.results[0] ? res.results[0].formatted_address : "";
      $("address").value = a;
      say(a ? "Location: " + a : "Pin placed. No address was found for this point.");
    }).catch(() => {
      $("address").value = "";
      say("The address lookup is unavailable. Your pin is kept and you can still submit.", true); // NF-09
    });
  }

  window.initReportMap = async function () {
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    await google.maps.importLibrary("geocoding");
    geocoder = new google.maps.Geocoder();
    map = new Map($("pick-map"), { center: CENTER, zoom: 14, mapId: "DEMO_MAP_ID", streetViewControl: false, mapTypeControl: false });
    marker = new AdvancedMarkerElement({ gmpDraggable: true });
    marker.addListener("dragend", () => setLocation(marker.position));
    map.addListener("click", (e) => setLocation(e.latLng));

    // keep an earlier choice after a failed submit
    if ($("latitude").value && $("longitude").value) {
      setLocation({ lat: Number($("latitude").value), lng: Number($("longitude").value) }, $("address").value);
    }

    // typed address with suggestions; falls back to a plain box that geocodes on change
    try {
      const { PlaceAutocompleteElement } = await google.maps.importLibrary("places");
      const ac = new PlaceAutocompleteElement({});
      $("address-box").appendChild(ac);
      const onSelect = async (e) => {
        const place = e.placePrediction ? e.placePrediction.toPlace() : e.place;
        await place.fetchFields({ fields: ["location", "formattedAddress"] });
        map.setZoom(17);
        setLocation(place.location, place.formattedAddress);
      };
      ac.addEventListener("gmp-select", onSelect);
      ac.addEventListener("gmp-placeselect", onSelect);
    } catch (err) {
      const input = document.createElement("input");
      input.type = "text"; input.id = "address-fallback"; input.placeholder = "Street and number";
      input.addEventListener("change", () => {
        geocoder.geocode({ address: input.value }).then((res) => {
          if (res.results[0]) setLocation(res.results[0].geometry.location, res.results[0].formatted_address);
          else say("Address not found. Try another spelling or tap the map.", true);
        }).catch(() => say("The address lookup is unavailable. Tap the map to place a pin.", true));
      });
      $("address-box").appendChild(input);
    }
  };

  $("use-location").addEventListener("click", () => {
    if (!navigator.geolocation) { say("Your browser cannot share its location. Type an address or tap the map.", true); return; }
    say("Finding your location…");
    navigator.geolocation.getCurrentPosition(
      (p) => { map.setZoom(17); setLocation({ lat: p.coords.latitude, lng: p.coords.longitude }); },
      () => say("Location access was denied. Type an address or tap the map to place a pin.", true), // NF-10
      { enableHighAccuracy: true, timeout: 10000 }
    );
  });

  $("photos").addEventListener("change", (e) => {
    const box = $("photo-preview"); box.innerHTML = "";
    Array.from(e.target.files).forEach((f) => { const i = document.createElement("img"); i.src = URL.createObjectURL(f); i.alt = "Selected photo"; box.appendChild(i); });
  });

  form.addEventListener("submit", (e) => {
    if (!$("latitude").value || !$("longitude").value) { e.preventDefault(); say("Choose a location first: use your position, type an address or tap the map.", true); $("pick-map").scrollIntoView({ block: "center" }); }
  });
})();
