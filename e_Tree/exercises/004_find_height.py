"""
Find the Height of a BST

Implement a function findHeight(root) which returns the height of a given binary search tree.

    1. Height of a Node — the number of edges between a node and its deepest descendent
    2. Height of a Tree — Height of its root node
Also, keep in mind that the height of an empty tree and leaf nodes is zero.
"""
from e_Tree.BST.binary_search_tree import BinarySearchTree


def find_height(root):
    if root is None:
        return -1
    else:
        max_sub_tree_height = max(
            find_height(root.leftChild),
            find_height(root.rightChild)
        )
        return 1 + max_sub_tree_height


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    BST.insert(10)
    BST.insert(14)
