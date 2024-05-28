from c_Queues_Stack.stacks import Stack
from d_Graph.a_adjacent_list.adjacent_list import Graph


def dfs_traversal_helper(g, src, visited):
    result = ""
    stack = Stack()
    stack.push(src)
    visited[src] = True

    while not stack.is_empty():
        current_node = stack.pop()
        result += str(current_node)
        head = g.array[current_node].head_node

        while head is not None:
            if not visited[head.data]:
                stack.push(head.data)
                visited[head.data] = True
            head = head.next_element

    return result, visited


def dfs_traversal(g, source):
    if g.vertices == 0:
        return ''
    visited = [False] * g.vertices

    result, visited = dfs_traversal_helper(g, source, visited)

    for i in range(g.vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new

    return result


if __name__ == "__main__":
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        g.print_graph()
        print(dfs_traversal(g, 1))
