const ciudadesData = {
    'Jiloyork': [19.916012, -99.580580],
    'Toluca': [19.289165, -99.655697],
    'Atlacomulco': [19.799520, -99.873844],
    'Guadalajara': [20.677754, -103.346254],
    'Monterrey': [25.691611, -100.321838],
    'QuintanaRoo': [21.163112, -86.802315],
    'Michohacan': [19.701400, -101.208297],
    'Aguascalientes': [21.876410, -102.264387],
    'CDMX': [19.432713, -99.133183],
    'QRO': [20.597194, -100.386670]
  };
  
  // Rellenar select
  const select = document.getElementById("ciudades");
  Object.keys(ciudadesData).forEach(ciudad => {
    const option = document.createElement("option");
    option.value = ciudad;
    option.textContent = ciudad;
    select.appendChild(option);
  });
  
  // Inicializar mapa
  const map = L.map('map').setView([20.0, -99.0], 5);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);
  
  let rutaLayer;
  
  async function resolver() {
    const seleccionadas = Array.from(select.selectedOptions).map(opt => opt.value);
    const response = await fetch("/resolver", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ciudades: seleccionadas })
    });
  
    const data = await response.json();
    const ruta = data.coordenadas;
  
    if (rutaLayer) map.removeLayer(rutaLayer);
  
    rutaLayer = L.polyline(ruta, { color: 'red', weight: 5 }).addTo(map);
    map.fitBounds(rutaLayer.getBounds());
  
    document.getElementById("resultado").innerText =
      `Ruta: ${data.ruta.join(" → ")} | Distancia total: ${data.distancia_total.toFixed(2)}`;
  }
  