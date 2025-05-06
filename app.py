from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from hilmiter import hill_climbing, coord  # Importar desde el archivo separado

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    data = request.get_json()
    ciudades = data.get('ciudades', list(coord.keys()))

    ruta, distancia_total = hill_climbing(ciudades, coord)
    coordenadas = [coord[ciudad] for ciudad in ruta]

    return jsonify({
        'ruta': ruta,
        'coordenadas': coordenadas,
        'distancia_total': distancia_total
    })

if __name__ == '__main__':
    app.run(debug=True)
