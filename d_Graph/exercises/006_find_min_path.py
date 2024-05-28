from c_Queues_Stack.queues import Queue
from c_Queues_Stack.stacks import Stack
from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
Find the Shortest Path Between Two Vertices

Implement the find_min() function which will take a directed graph and two vertices, A and B. 
The result will be the shortest path from A to B.
Remember, the shortest path will contain the minimum number of edges.

"""


def find_min_path_bfs(g, source, destination):
    """
    O(V + E)
    :param g:
    :param source:
    :param destination:
    :return:
    """
    distance = [0] * g.vertices
    visited = [False] * g.vertices

    queue = Queue()
    queue.enqueue(source)
    visited[source] = True

    while queue.is_empty() is False:
        current = queue.dequeue()
        head = g.array[current].head_node

        while head is not None:
            if visited[head.data] is False:
                queue.enqueue(head.data)
                visited[head.data] = True

                distance[head.data] = distance[current] + 1  # KEY !!!

            if head.data == destination:
                return distance[destination]

            head = head.next_element

    return -1


def find_min_path_dfs(g, source, destination):
    """

    :param g:
    :param source:
    :param destination:
    :return:
    """
    visited = [False] * g.vertices
    distance = [0] * g.vertices
    stack = Stack()
    stack.push(source)
    visited[source] = True

    while not stack.is_empty():
        current = stack.pop()
        head = g.array[current].head_node

        while head:
            if visited[head.data] is False:
                visited[head.data] = True
                distance[head.data] = distance[current] + 1
                stack.push(head.data)

            if head.data == destination:
                return distance[destination]

            head = head.next_element

    return -1


if __name__ == '__main__':
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    print(find_min_path_bfs(g, 1, 5))
    print(find_min_path_dfs(g, 1, 5))
