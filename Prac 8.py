import sys

def dijkstra(graph, src):
    V = len(graph)
    dist = [float('inf')] * V
    dist[src] = 0
    visited = [False] * V
    for _ in range(V):
        min_dist = float('inf')
        u = -1
        for v in range(V):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        if u == -1:
            break
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t\t{dist[i]}")

graph = [
    [0, 4, 8, 0, 0, 0, 0, 11, 0],
    [4, 0, 0, 8, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 7, 4, 0, 0, 2],
    [0, 8, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 9, 14, 0, 0],
    [0, 0, 4, 0, 9, 0, 10, 0, 0],
    [0, 0, 0, 7, 14, 10, 0, 2, 0],
    [11, 0, 0, 0, 0, 0, 2, 0, 1],
    [0, 0, 2, 0, 0, 0, 0, 1, 0]
]

dijkstra(graph, 0)
