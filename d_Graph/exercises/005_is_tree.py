from typing import List

from d_Graph.a_adjacent_list.adjacent_list import Graph

"""
Check if a Given **Undirected Graph** is Tree or not?

Here’s the basic difference between a graph and a tree. A graph can only be a tree under two conditions:
    1. There are no cycles.
    2. The graph is connected.
    
A graph is connected when there is a path between every pair of vertices. 
In a connected graph, there are no unreachable vertices. 
Each vertex must be connected to every other vertex through either a direct edge or a graph traversal.

Tree
       ┌────┐
       │  0 │
       └──┬─┘
          │
     ┌────┴─────┐
     │          │
  ┌──┴─┐      ┌─┴──┐
  │  1 │      │  2 │
  └────┘      └────┘

Cycle Graph
    ┌───┐
    │ 0 ├──────────┐
    └─┬─┘          │
      │            │
      │            │
      │          ┌───┐
      │          │ 2 │
      │          └─┬─┘
    ┌───┐          │
    │ 1 │──────────┘
    └───┘


You have to implement is_tree() function which will take a graph as an input and find out if it is a tree.
"""


def is_tree(g: Graph):
    visited = [False] * g.vertices
    if check_cycle(g, 0, visited, -1):
        return False

    for i in range(len(visited)):
        # all vertex is connected
        if visited[i] is False:
            return False

    return True


def check_cycle(g: Graph, node: int, visited: List[bool], parent: int):
    visited[node] = True
    adjacent = g.array[node].head_node

    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node):
                return True
        # The only difference is that we keep track of the parent vertex since a backward link to the parent
        # does not count as a cycle (undirected graph).

        # 表示訪問過的節點，若 parent == adjacent.data 表示 bi-direction graph，並不是cycle graph
        elif adjacent.data is not parent:
            return True

        adjacent = adjacent.next_element

    return False


if __name__ == "__main__" :
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))
