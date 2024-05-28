from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
You have to implement the num_edges() function which takes an **undirected graph** 
and computes the total number of bidirectional edges.
"""


def num_edges(g):
    return sum([g.array[i].length() for i in range(g.vertices)]) // 2


if __name__ == '__main__':
    graph = Graph(9, is_directed=False)
    graph.add_edge(0, 2)
    graph.add_edge(0, 5)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(5, 3)
    graph.add_edge(5, 6)
    graph.add_edge(3, 6)
    graph.add_edge(6, 7)
    graph.add_edge(6, 8)
    graph.add_edge(6, 4)
    graph.add_edge(7, 8)

    graph_2 = Graph(7, is_directed=False)
    graph_2.add_edge(1, 2)
    graph_2.add_edge(1, 3)
    graph_2.add_edge(3, 4)
    graph_2.add_edge(3, 5)
    graph_2.add_edge(2, 5)
    graph_2.add_edge(2, 4)
    graph_2.add_edge(4, 6)
    graph_2.add_edge(4, 5)
    graph_2.add_edge(6, 5)

    print(num_edges(graph))
    print(num_edges(graph_2))
