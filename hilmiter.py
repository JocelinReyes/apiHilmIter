import random
import math

# Coordenadas de ciudades
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346254),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163112, -86.802315),
    'Michohacan': (19.701400, -101.208297),
    'Aguascalientes': (21.876410, -102.264387),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def evalua_ruta(ruta, coord_map):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord_map[ruta[i]], coord_map[ruta[i + 1]])
    total += distancia(coord_map[ruta[-1]], coord_map[ruta[0]])
    return total

def hill_climbing(ciudades, coord_map, iteraciones=10):
    mejor_ruta = None
    mejor_distancia = float('inf')

    for _ in range(iteraciones):
        ruta = ciudades[:]
        random.shuffle(ruta)
        mejora = True

        while mejora:
            mejora = False
            dist_actual = evalua_ruta(ruta, coord_map)

            for i in range(len(ruta)):
                for j in range(i + 1, len(ruta)):
                    nueva = ruta[:]
                    nueva[i], nueva[j] = nueva[j], nueva[i]
                    dist_nueva = evalua_ruta(nueva, coord_map)
                    if dist_nueva < dist_actual:
                        ruta = nueva
                        mejora = True
                        break
                if mejora:
                    break

        if evalua_ruta(ruta, coord_map) < mejor_distancia:
            mejor_ruta = ruta[:]
            mejor_distancia = evalua_ruta(ruta, coord_map)

    return mejor_ruta, mejor_distancia
