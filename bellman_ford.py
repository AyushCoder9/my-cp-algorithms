#Question
'''Bellman-Ford algorithm to find the shortest path from a source vertex to all other vertices.'''

def bellman_ford(vertices, edges, source):
    distances = [float('inf')] * vertices
    distances[source] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            print("Graph contains negative weight cycle")
            return None

    return distances

v = 5
e = [
    (0, 1, -1), (0, 2, 4),
    (1, 2, 3), (1, 3, 2), (1, 4, 2),
    (3, 2, 5), (3, 1, 1), (4, 3, -3)
]
src = 0
print(f"Shortest distances from source {src}:", bellman_ford(v, e, src))
