
# -------------------------------
# Undirected Graph using Adjacency List
# -------------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Undirected Graph Representation:")
for node in graph:
    print(node, "->", graph[node])


# -------------------------------
# Depth First Search (DFS) - Recursive
# -------------------------------
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("\n\nDFS Traversal starting from 'A':")
dfs(graph, 'A')


# -------------------------------
# Breadth First Search (BFS)
# -------------------------------
from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


print("\n\nBFS Traversal starting from 'A':")
bfs(graph, 'A')