def distance_vector_routing(vertices, adj_matrix):
    """
    Implements the Distance Vector Routing algorithm (Bellman-Ford variant).
    The algorithm computes the shortest paths between all pairs of nodes
    using the adjacency matrix as input.
    """
    V = len(adj_matrix)
    distance = [[float('inf')] * V for _ in range(V)]  # Initialize distances with infinity

    # Set the distance of each node to itself as 0
    for i in range(V):
        for j in range(V):
            if i == j:
                distance[i][j] = 0
            elif adj_matrix[i][j] != 0:
                distance[i][j] = adj_matrix[i][j]

    # Run Distance Vector Routing algorithm (Bellman-Ford)
    for k in range(V):  # Intermediate node
        for i in range(V):  # Source node
            for j in range(V):  # Destination node
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Get user input for the graph
num_vertices = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix (use 0 for no path):")
for i in range(num_vertices):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    graph.append(row)

# Run Distance Vector Routing
distances = distance_vector_routing(num_vertices, graph)

# Output the distance vectors for each node
print("Distance vector for each node:")
for i in range(num_vertices):
    print(f"Node {i}: {distances[i]}")
