class DisjointSet:

    def __init__(self, vertices):
        # Parent dictionary stores parent of each vertex
        self.parent = {v: v for v in vertices}

        # Rank dictionary helps in union by rank optimization
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        # Find the root parent of the vertex
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, v1, v2):
        # Find roots of both vertices
        root1 = self.find(v1)
        root2 = self.find(v2)

        # If roots are different, union them
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_mst(vertices, edges):

    # Sort edges based on weight (Greedy choice)
    edges = sorted(edges, key=lambda x: x[2])

    # Create disjoint set
    ds = DisjointSet(vertices)

    mst = []   # List to store MST edges
    total_weight = 0

    for edge in edges:
        u, v, weight = edge

        # Check if including this edge forms a cycle
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append(edge)
            total_weight += weight
            print(f"Selected Edge: {edge}")

    return mst, total_weight

# Example Graph
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

mst, weight = kruskal_mst(vertices, edges)

print("\nMinimum Spanning Tree:", mst)
print("Total Weight of MST:", weight)
