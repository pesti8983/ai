import heapq

def prim_mst(graph, start):

    visited = set([start])
    edges = []
    total_weight = 0

    # Priority queue (min-heap)
    min_heap = []

    # Add all edges from start node
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    # Process until all vertices are covered
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            edges.append((u, v, weight))
            total_weight += weight

            print(f"Selected Edge: ({u}, {v}, {weight})")

            # Add edges of new vertex
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, v, neighbor))

    return edges, total_weight


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('A', 3), ('B', 2), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}


# ------------------------------------------
# Main Execution
# ------------------------------------------
if __name__ == "__main__":

    mst, weight = prim_mst(graph, 'A')

    print("\nMinimum Spanning Tree:", mst)
    print("Total Weight of MST:", weight)