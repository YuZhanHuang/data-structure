"""
Find Nodes at "k" distance from the Root

Implement a function find_k_nodes(root,k) which finds and returns nodes
at k distance from the root in the given binary tree.
"""
from e_Tree.BST.binary_search_tree import BinarySearchTree


def find_k_nodes(root, k):
    res = []
    find_k_recur(root, k, res)  # recurse the tree for node at k distance
    return res


def find_k_recur(root, k, res):
    if root is None:  # return if root does not exist
        return
    if k == 0:
        res.append(root.val)  # append as root is kth node
    else:
        # check recursively in both subtree for kth node
        find_k_recur(root.left_child, k - 1, res)
        find_k_recur(root.right_child, k - 1, res)


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    print(find_k_nodes(BST.root, 2))
