import heapq

def find_components(graph):
    """
    Realiza una búsqueda en anchura (BFS) para encontrar todas las componentes conexas.
    Retorna una lista de listas, donde cada sublista contiene los vértices de una componente.
    """
    visited = set()
    components = []
    
    vertices = graph.get_vertices()
    for vertex in vertices:
        if vertex not in visited:
            # Nuevo componente encontrado, iniciamos BFS
            component = []
            queue = [vertex]
            visited.add(vertex)
            
            while queue:
                current = queue.pop(0)
                component.append(current)
                
                for neighbor in graph.adj_list.get(current, {}):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(component)
            
    return components

def is_bipartite(graph, component):
    """
    Comprueba si el subgrafo formado por la lista de vértices en 'component' es bipartito.
    Usa BFS bicoloreado. Retorna True o False.
    """
    if not component:
        return True
        
    color_map = {}
    # Podría haber componentes desconectados dentro del parámetro (aunque por diseño viene conexo), iteramos de manera segura.
    for start_node in component:
        if start_node not in color_map:
            color_map[start_node] = 0
            queue = [start_node]
            
            while queue:
                current = queue.pop(0)
                current_color = color_map[current]
                
                for neighbor in graph.adj_list.get(current, {}):
                    if neighbor in component: # Solo consideramos nodos en la componente
                        if neighbor not in color_map:
                            # Asignamos el color opuesto (1 - color actual)
                            color_map[neighbor] = 1 - current_color
                            queue.append(neighbor)
                        elif color_map[neighbor] == current_color:
                            # Mismo color en nodos adyacentes = no es bipartito
                            return False
    return True

# --- Estructura Disjoint-Set / Union-Find para Kruskal ---
class DisjointSet:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}
        
    def find(self, item):
        if self.parent[item] == item:
            return item
        # Path compression Optimization
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
        
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        
        if root1 != root2:
            # Union by Rank Optimization
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def kruskal_mst(graph, component):
    """
    Encuentra el Árbol de Expansión Mínimo para una componente específica usando Kruskal.
    Retorna (peso_total_mst, lista_de_aristas)
    """
    component_set = set(component)
    edges = []
    
    # Extraer aristas válidas de esta componente
    visited_edges = set()
    for u in component:
        for v, weight in graph.adj_list.get(u, {}).items():
            if v in component_set:
                edge_pair = tuple(sorted([u, v]))
                if edge_pair not in visited_edges:
                    visited_edges.add(edge_pair)
                    edges.append((weight, u, v))
                    
    # Kruskal requiere ordenar aristas por peso
    edges.sort(key=lambda x: x[0])
    
    ds = DisjointSet(component)
    mst_weight = 0.0
    mst_edges = []
    
    for weight, u, v in edges:
        if ds.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            
    return mst_weight, mst_edges

def dijkstra(graph, source):
    """
    Encuentra los caminos mínimos desde 'source' a todos los demás vértices.
    Usa el montículo predeterminado de Python (heapq) para optimización.
    Retorna un diccionario con 'distances' y 'previous_nodes'.
    """
    # Explicación de estructura de retorno:
    # distances[v] -> distancia mínima desde 'source' a 'v'
    # prev[v] -> predecesor de 'v' en el camino mínimo. Útil para reconstruir camino.
    
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    prev = {vertex: None for vertex in graph.get_vertices()}
    distances[source] = 0.0
    
    # Cola de prioridad que almacena tuplas (distanciaacumulada, vertice)
    pq = [(0.0, source)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Si sacamos un registro obsoleto de la cola (por Python heapq al no borrar) lo ignoramos:
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph.adj_list.get(current_vertex, {}).items():
            distance = current_distance + weight
            
            # Camino más costo-efectivo encontrado
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
                
    return {'distances': distances, 'previous_nodes': prev}

def get_shortest_path(dijkstra_result, target):
    """
    Reconstruye el camino camino desde el diccionario resultante de dijkstra.
    Retorna la lista de vértices en orden desde el origen hasta el 'target',
    o una lista vacía si no existe camino o el target es inalcanzable.
    """
    prev = dijkstra_result['previous_nodes']
    path = []
    current = target
    
    # Si su predecesor es None y no es el source de origen (cuya distancia seria 0), es inalcanzable
    if prev.get(current) is None and dijkstra_result['distances'].get(current, float('inf')) != 0:
        return []

    while current is not None:
        path.insert(0, current)
        current = prev.get(current)
        
    return path
