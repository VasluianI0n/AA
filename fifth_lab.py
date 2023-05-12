import numpy as np
import time
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    n = len(graph)
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    visited = set()

    while len(visited) < n:
        current_node = min(
            set(distances.keys()) - visited,
            key=lambda x: distances[x]
        )
        visited.add(current_node)

        for neighbor in range(n):
            if graph[current_node][neighbor] != float('inf'):
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


def floyd_warshall(graph):
    n = len(graph)
    dist = np.copy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = np.array([
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
])

start_time = time.time()
dijkstra_distances = dijkstra(graph, 0)
dijkstra_execution_time = time.time() - start_time

start_time = time.time()
floyd_distances = floyd_warshall(graph)
floyd_execution_time = time.time() - start_time

print("Dijkstra's Shortest Distances:")
for node, distance in dijkstra_distances.items():
    print(f"From 0 to {node}: {distance}")

print("\nFloyd-Warshall Shortest Distances:")
for i in range(len(graph)):
    for j in range(len(graph)):
        print(f"From {i} to {j}: {floyd_distances[i][j]}")

# Plotting execution times
algorithms = ['Dijkstra', 'Floyd-Warshall']
execution_times = [dijkstra_execution_time, floyd_execution_time]

plt.plot(algorithms, execution_times, marker='*', color='r', linestyle='-', linewidth=2)
plt.xlabel('Algorithm')
plt.ylabel('Execution Time (seconds)')
plt.title('Dijkstra and Floyd-Warshall Algorithms execution Time')
plt.grid(True)
plt.show()