// getting the iss position
let latitude;
let longitude;
// let map, marker;

apiUrl = "http://api.open-notify.org/iss-now.json";

var map = L.map("map").setView([0, 0], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 4,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

const myIcon = L.icon({
  iconUrl: "/static/img/iss-icon.png",
  // iconUrl: "{{ url_for('static', filename='img/iss-icon.png') }}",
  iconSize: [38, 38], // size of the icon
  iconAnchor: [19, 19], // point of the icon which will correspond to marker's location
});

var marker = L.marker([0, 0], { icon: myIcon }).addTo(map);

function updateISSPosition() {
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      latitude = data.iss_position.latitude;
      longitude = data.iss_position.longitude;
      console.log(`Lat: ${latitude}, Lon: ${longitude}`);

      marker.setLatLng([latitude, longitude]);
      map.setView([latitude, longitude]);
    })
    .catch((error) => {
      console.error("Error fetching ISS position:", error);
    });
}
setInterval(updateISSPosition, 5000);
