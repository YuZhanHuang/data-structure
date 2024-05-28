from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
The concept of loops or cycles is very common in graph theory. 
A cycle exists when you traverse the **directed graph** and come upon a vertex that has already been visited.
You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.
"""


def detect_cycle_rec(g, node, visited, rec_node_stack) -> bool:
    # Base Case
    if rec_node_stack[node]:
        return True
    if visited[node]:
        return False

    rec_node_stack[node] = True
    visited[node] = True
    head_node = g.array[node].head_node

    while head_node is not None:
        adjacent = head_node.data
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next_element

    rec_node_stack[node] = False
    return False


def detect_cycle(g: Graph) -> bool:
    if g.vertices == 0:
        return False
    rec_node_stack = [False] * g.vertices
    visited = [False] * g.vertices

    for node in range(g.vertices):
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False


if __name__ == '__main__':
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 1)

    print('g1', detect_cycle(g1))
    print('g2', detect_cycle(g2))
