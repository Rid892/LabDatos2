import csv
import math

# Haversine formula to calculate the distance between two geographical points
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radio de la Tierra en kilómetros
    
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2.0)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0)**2
        
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

class FlightGraph:
    def __init__(self):
        # self.adj_list: dict[str, dict[str, float]]
        # Mapa de código de aeropuerto a un diccionario de destinos y pesos
        self.adj_list = {}
        
        # self.airports: dict[str, dict]
        # Almacena metadatos de los aeropuertos (Nombre, Ciudad, País, Latitud, Longitud)
        self.airports = {}
        
    def add_airport(self, code, name, city, country, lat, lon):
        if code not in self.airports:
            self.airports[code] = {
                'code': code,
                'name': name,
                'city': city,
                'country': country,
                'lat': float(lat),
                'lon': float(lon)
            }
            if code not in self.adj_list:
                self.adj_list[code] = {}

    def add_edge(self, source, dest, weight):
        # Es un grafo no dirigido simple
        if dest not in self.adj_list[source]:
            self.adj_list[source][dest] = weight
        if source not in self.adj_list[dest]:
            self.adj_list[dest][source] = weight

    def load_from_csv(self, filepath):
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Extraemos Aeropuerto Origen
                src_code = row['Source Airport Code']
                src_lat = float(row['Source Airport Latitude'])
                src_lon = float(row['Source Airport Longitude'])
                self.add_airport(
                    code=src_code,
                    name=row['Source Airport Name'],
                    city=row['Source Airport City'],
                    country=row['Source Airport Country'],
                    lat=src_lat,
                    lon=src_lon
                )
                
                # Extraemos Aeropuerto Destino
                dst_code = row['Destination Airport Code']
                dst_lat = float(row['Destination Airport Latitude'])
                dst_lon = float(row['Destination Airport Longitude'])
                self.add_airport(
                    code=dst_code,
                    name=row['Destination Airport Name'],
                    city=row['Destination Airport City'],
                    country=row['Destination Airport Country'],
                    lat=dst_lat,
                    lon=dst_lon
                )
                
                # Calculamos el peso (distancia) solo si no existe la misma arista con otro peso
                # Es grafo simple, por lo que una arista por par de vértices es suficiente
                if dst_code not in self.adj_list[src_code]:
                    distance = haversine_distance(src_lat, src_lon, dst_lat, dst_lon)
                    self.add_edge(src_code, dst_code, distance)

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        # Retorna todas las aristas (u, v, peso) evitando duplicados
        edges = []
        visited = set()
        for u in self.adj_list:
            for v, weight in self.adj_list[u].items():
                # Para grafo no dirigido, (u, v) es igual a (v, u)
                edge = tuple(sorted([u, v]))
                if edge not in visited:
                    visited.add(edge)
                    edges.append((edge[0], edge[1], weight))
        return edges
