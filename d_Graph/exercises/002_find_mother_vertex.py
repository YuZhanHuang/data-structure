from c_Queues_Stack.stacks import Stack
from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
You have to implement the find_mother_vertex() function which will take a **directed graph** as an input and 
find out which vertex is the mother vertex in the graph.

By definition, the mother vertex is a vertex in a graph such that 
all other vertices in a graph can be reached by following a path from that vertex. 
A graph can have multiple mother vertices,
 
** but you only need to find one. **

Mother Vertices 0, 1, 2
         ┌───┐
         │ 0 │◄──────┐
         └─┬─┘       │
           │         │
           │         │
           │         │
           ▼         │
         ┌───┐       │
         │ 1 │       │
         └─┬─┘       │
           │         │
           │         │
           │         │
           ▼         │
         ┌───┐       │
         │ 2 │       │
         └─┬─┘       │
           │         │
           └─────────┘

Mother Vertex 3
        ┌───┐
        │ 3 ├──────────┐
        └─┬─┘          │
          │            │
          │            │
          │          ┌─▼─┐
          │          │ 0 │
          │          └─┬─┘
        ┌─▼─┐          │
        │ 1 │◄─────────┘
        └─┬─┘
          │
          │
          │
        ┌─▼─┐
        │ 2 │
        └───┘
"""


def find_mother_vertex(g: Graph) -> int:
    """
    O(V(V + E))
    :param g:
    :return:
    """
    num_of_vertices = g.vertices

    for i in range(g.vertices):
        # dfs will visit all vertices.
        if perform_dfs(g, i) == num_of_vertices:
            return i

    return -1


def perform_dfs(g: Graph, source: int) -> int:
    """
    return vertices_reached
    :param g:
    :param source:
    :return:
    """
    visited = [False] * g.vertices
    stack = Stack()
    stack.push(source)
    visited[source] = True
    vertices_reached = 0

    while not stack.is_empty():
        current_node = stack.pop()
        head_node = g.array[current_node].head_node

        while head_node is not None:
            if visited[head_node.data] is False:
                stack.push(head_node.data)
                visited[head_node.data] = True
                vertices_reached += 1

            head_node = head_node.next_element

    return vertices_reached + 1


def find_mother_vertex_v2(g: Graph):
    """
    Kosaraju’s Strongly Connected Component Algorithm
    O(V + E)
    :param g: Graph
    :return:
    """
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False] * g.vertices

    # To store last finished vertex (or mother vertex)
    last_v = 0

    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if not visited[i]:
            perform_dfs_v2(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vertices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.

    visited = [False] * g.vertices
    perform_dfs_v2(g, last_v, visited)
    if any(not i for i in visited):  # any() func iterates over a list
        return -1
    else:
        return last_v


# A recursive function to print DFS starting from v
# NOTE: 比較與traversal裡面的使用stack的版本 dfs_traversal
def perform_dfs_v2(g, node, visited):
    # Mark the current node as visited and print it
    visited[node] = True
    # Recur for all the vertices adjacent to this vertex
    head = g.array[node].head_node
    while head:
        if not visited[head.data]:
            perform_dfs_v2(g, head.data, visited)
        head = head.next_element


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print(find_mother_vertex(g))
    print(find_mother_vertex_v2(g))
