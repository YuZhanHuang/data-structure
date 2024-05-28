"""
Find kth maximum value in Binary Search Tree

Implement a function find_kth_max(root,k)
which will take a BST and any number “k” as an input and return kth maximum number from that tree.

"""
from e_Tree.BST.binary_search_tree import BinarySearchTree


def find_kth_max(root, k):
    tree = []
    in_order_traverse(root, tree)  # Get sorted tree list
    if ((len(tree) - k) >= 0) and (k > 0):  # check if k is valid
        return tree[-k]  # return the kth max value
    return None  # return none if no value found


def in_order_traverse(node, tree):
    # Helper recursive function to traverse the tree inorder
    if node is not None:  # check if node exists
        in_order_traverse(node.left_child, tree)  # traverse left sub-tree
        if len(tree) == 0:
            # Append if empty tree
            tree.append(node.val)
        elif tree[-1] is not node.val:
            # Ensure not a duplicate
            tree.append(node.val)  # add current node value
        in_order_traverse(node.right_child, tree)  # traverse right sub-tree


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)

    print(find_kth_max(BST.root, 4))
