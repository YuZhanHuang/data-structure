class Graph:
    def __init__(self, size, is_directed=False):
        self.adjMatrix = [
            [0 for _ in range(size)] for _ in range(size)
        ]
        self.size = size
        self.is_directed = is_directed

    def add_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size or v1 < 0 or v2 < 0:
            raise ValueError("Invalid vertex number")

        self.adjMatrix[v1][v2] = 1

        if self.is_directed is False:
            self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size or v1 < 0 or v2 < 0:
            raise ValueError("Invalid vertex number")
        self.adjMatrix[v1][v2] = 0

        if self.is_directed is False:
            self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.adjMatrix])


if __name__ == '__main__':
    graph = Graph(4)  # Create a graph with 4 vertices
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    print(graph)
