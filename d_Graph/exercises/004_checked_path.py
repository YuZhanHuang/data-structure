from c_Queues_Stack.queues import Queue
from c_Queues_Stack.stacks import Stack
from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
You have to implement the check_path() function.
It takes a source vertex and a destination vertex and tells us whether or not a path exists between the two.
"""


def check_path_dfs(g, source, destination):
    """
    O(V + E)
    :param g:
    :param source:
    :param destination:
    :return:
    """
    visited = [False] * g.vertices
    stack = Stack()
    stack.push(source)
    visited[source] = True

    while not stack.is_empty():
        current = stack.pop()
        if current == destination:
            return True
        head_node = g.array[current].head_node

        while head_node is not None:
            if visited[head_node.data] is False:
                stack.push(head_node.data)
                visited[head_node.data] = True

            head_node = head_node.next_element

    return False


def check_path_bfs(g, source, destination):
    """
    O(V + E)
    :param g:
    :param source:
    :param destination:
    :return:
    """
    # BFS to check path between source and dest
    # Keep track of visited vertices
    visited = [False] * g.vertices

    # Create a queue for BFS
    queue = Queue()

    # Enqueue source and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Loop to traverse the whole graph using BFS
    while not queue.is_empty():
        node = queue.dequeue()

        # Check if dequeued node is the destination
        if node is destination:
            return True

        # Continue BFS by obtaining first element in linked list
        adjacent = g.array[node].head_node
        while adjacent:
            # enqueue adjacent node if it has not been visited
            if not visited[adjacent.data]:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element

    # Destination was not found in the search
    return False


if __name__ == '__main__':
    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    print(check_path_dfs(g1, 0, 7))
    print(check_path_dfs(g2, 3, 0))

    print(check_path_bfs(g1, 0, 7))
    print(check_path_bfs(g2, 3, 0))
