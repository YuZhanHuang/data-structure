from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
You must implement the remove_edge function which takes a source and a destination as arguments. 
If an edge exists between the two, it should be deleted.
"""


def delete_edge(graph: Graph, source, destination):
    if not graph:
        return graph

    if source >= len(graph.array) or source < 0:
        return graph

    if destination >= len(graph.array) or destination < 0:
        return graph

    graph.array[source].delete(destination)

    return graph


if __name__ == '__main__':
    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 0)

    g.print_graph()

    delete_edge(g, 1, 3)
    print('========== After Deletion ==========')
    g.print_graph()
