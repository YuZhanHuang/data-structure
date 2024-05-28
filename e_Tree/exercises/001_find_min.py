"""
Find minimum value in Binary Search Tree

Implement the find_min(root) function which will find the minimum value in a given Binary Search Tree.
Remember, a Binary Search Tree is a Binary Tree which satisfies the following property.

NodeValues(LeftSubtree) <= CurrentNodeValue < NodeValues(RightSubTree)

"""
from e_Tree.BST.binary_search_tree import BinarySearchTree


def find_min_iter(root):
    if root is None:  # check for None
        return None
    while root.left_child:  # Traverse until the last child
        root = root.left_child
    return root.val  # return the last child


def find_min_recur(root):
    if root is None:  # check if root exists
        return None
    elif root.left_child is None:  # check if left child exists
        return root.val  # return if not left child
    else:
        return find_min_recur(root.left_child)  # recurse onto the left child


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    BST.insert(20)
    BST.insert(3)
    BST.insert(54)
    BST.insert(6)
    print(find_min_recur(BST.root))
