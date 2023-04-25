from collections import defaultdict
import time
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = {s}
        queue = [s]
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = {v}
        self.dfs_util(v, visited)


if __name__ == '__main__':
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS:")
    start_time = time.time()
    g.bfs(2)
    bfs_time = time.time() - start_time
    print(f"\nBFS time: {bfs_time:.8f} seconds")

    print("\nDFS:")
    start_time = time.time()
    g.dfs(2)
    dfs_time = time.time() - start_time
    print(f"\nDFS time: {dfs_time:.8f} seconds")

    plt.plot(['BFS'], [bfs_time], 'c.', label="BFS")
    plt.plot(['DFS'], [dfs_time], 'm*', label="DFS")
    plt.xlabel('Algorithm')
    plt.ylabel('Time (s)')
    plt.title('Graph for BFS and DFS')
    plt.legend()
    plt.show()