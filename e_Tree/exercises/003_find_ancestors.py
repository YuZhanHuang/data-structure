"""
Find Ancestors of a given node in a BST

Implement the find_ancestors(root, k) function which will find the ancestors of the node whose value is “k”.
Here root is the root node of a binary search tree and k is an integer value of node whose ancestors you need to find.

"""
from e_Tree.BST.binary_search_tree import BinarySearchTree


def find_ancestors(root, k):
    result = []
    rec_find_ancestors(root, k, result)  # recursively find ancestors
    return result  # return a string of ancestors


def rec_find_ancestors(root, k, result):
    if root is None:  # check if root exists
        return False
    elif root.val is k:  # check if val is k
        return True
    recur_left = rec_find_ancestors(root.leftChild, k, result)
    recur_right = rec_find_ancestors(root.rightChild, k, result)
    if recur_left or recur_right:
        # if recursive find in either left or right subtree
        # append root value and return true
        result.append(root.val)
        return True
    return False  # return false if all failed


def find_ancestors_v2(root, k):
    if not root:  # check if root exists
        return None
    ancestors = []  # empty list of ancestors
    current = root  # iterator current set to root

    while current is not None:  # iterate until we reach None
        if k > current.val:  # go right
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:  # go left
            ancestors.append(current.val)
            current = current.leftChild
        else:  # when k == current.val
            return ancestors[::-1]
    return []


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    BST.insert(1)
    BST.insert(133)
    BST.insert(12)
    print(find_ancestors(BST.root, 12))
