class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, val):
        """
        配合BinarySearchTree，current指的就會是root
        :param val:
        :return:
        """
        current = self
        parent = None

        # 從根結點開始往下找
        while current:
            parent = current
            if val < current.val:
                current = current.left_child
            else:
                current = current.right_child

        if val < parent.val:
            parent.left_child = Node(val)
        else:
            parent.right_child = Node(val)

    def search(self, val):
        current = self

        while current:
            if val < current.val:
                current = current.left_child
            elif val > current.val:
                current = current.right_child
            else:
                return True, current

        return False, None

    def delete(self, val):
        # if current node's val is less than that of root node,
        # then only search in left subtree otherwise right subtree
        if val < self.val:
            if self.left_child:
                self.left_child = self.left_child.delete(val)
            else:
                print(str(val) + " not found in the tree", self.val)
                return self
        elif val > self.val:
            if self.right_child:
                self.right_child = self.right_child.delete(val)
            else:
                print(str(val) + " not found in the tree", self.val)
                return self
        else:
            # deleting node with no children
            if self.left_child is None and self.right_child is None:
                return
            # deleting node with right child
            elif self.left_child is None:
                return self.right_child
            # deleting node with left child
            elif self.right_child is None:
                return self.left_child
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.right_child

                # loop down to find the leftmost leaf
                while current.left_child is not None:
                    current = current.left_child

                self.val = current.val
                self.right_child = self.right_child.delete(current.val)

        return self


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def get_root(self):
        return self.root

    def insert(self, val):
        self.root.insert(val)

    def search(self, val):
        return self.root.search(val)

    def delete(self, val):
        return self.root.delete(val)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left_child)
        print(f'{root.val} ->', end=' ')
        self.inorder(root.right_child)

    def preorder(self, root):
        if root is None:
            return
        print(f'{root.val} ->', end=' ')
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left_child)
        self.postorder(root.right_child)
        print(f'{root.val} ->', end=' ')


if __name__ == '__main__':
    BST = BinarySearchTree(6)
    root_node = BST.get_root()
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    BST.delete(13)
    print('Traversal a Binary Tree')
    print('---------- postorder ----------')

    # print postorder traversal
    BST.postorder(root_node)
    print('\n')
    print('---------- preorder ----------')

    # print preorder traversal
    BST.preorder(root_node)
    print('\n')
    print('---------- inorder ----------')

    # print inorder traversal
    BST.inorder(root_node)
    print('\n')
