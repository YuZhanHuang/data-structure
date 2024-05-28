from c_Queues_Stack.queues import Queue
from d_Graph.a_adjacent_list.adjacent_list import Graph


def bfs_traversal_helper(g, src, visited):
    result = ''
    queue = Queue()
    queue.enqueue(src)
    visited[src] = True

    while not queue.is_empty():
        current_node = queue.dequeue()
        result += str(current_node)

        head = g.array[current_node].head_node
        while head is not None:
            if visited[head.data] is False:
                queue.enqueue(head.data)
                visited[head.data] = True

            head = head.next_element

    return result, visited


def bfs_traversal(g, source):
    if g.vertices == 0:
        return ''

    visited = [False] * g.vertices
    result, visited = bfs_traversal_helper(g, source, visited)

    for i in range(g.vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new

    return result


if __name__ == "__main__":
    graph = Graph(4)
    num_of_vertices = graph.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        graph.print_graph()
        print('Start from <Node 0>')
        print(bfs_traversal(graph, 0))
