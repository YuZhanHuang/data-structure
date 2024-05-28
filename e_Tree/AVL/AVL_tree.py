class TreeNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.key)


class AVLTree:

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Update the balance factor and balance the tree
        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            # LL Case
            if key < root.left.key:
                return self.right_rotate(root)
            # LR Case
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            # RR Case
            if key > root.right.key:
                return self.left_rotate(root)
            # RL Case
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)

        # FIXME Why ??????
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_factor = self.get_balance(root)

        # Balance the tree
        if balance_factor > 1:
            # LL Case
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            # LR Case
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            # RR Case
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            # RL Case
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    # Function to perform left rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)

        return y

    # Function to perform right rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        self.update_height(z)
        self.update_height(y)

        return y

    # Get the height of the node
    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    # Get balance factor of the node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.key), end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

    # Print the tree
    @staticmethod
    def print_helper(root_):
        space_symbol = r" "
        spaces_count = 4 * 2 ** root_.height
        out_string = r""
        initial_spaces_string = space_symbol * spaces_count + "\n"
        if not root_:
            return "Tree is empty"
        height = 2 ** root_.height
        level = [root_]

        while len([i for i in level if (i is not None)]) > 0:
            level_string = initial_spaces_string
            for i in range(len(level)):
                j = int((2 * i + 1) * spaces_count / (2 * len(level)))
                level_string = level_string[:j] + str(level[i] if level[i] else space_symbol) + level_string[j + 1:]
            out_string += level_string

            # create next level
            level_next = []
            for i in level:
                level_next += ([i.left, i.right]
                               if i else [None, None])
            # add connection to the next nodes
            for w in range(height - 1):
                level_string = initial_spaces_string
                for i in range(len(level)):
                    if not level[i] is None:
                        shift = spaces_count // (2 * len(level))
                        j = (2 * i + 1) * shift
                        level_string = level_string[:j - w - 1] + (
                            '/' if level[i].left else
                            space_symbol) + level_string[j - w:]
                        level_string = level_string[:j + w + 1] + (
                            '\\' if level[i].right else
                            space_symbol) + level_string[j + w:]
                out_string += level_string
            height = height // 2
            level = level_next

        print(out_string)


if __name__ == '__main__':
    myTree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = myTree.insert_node(root, num)
    myTree.print_helper(root)
    key = 13
    root = myTree.delete_node(root, key)
    print("After Deletion: ")
    myTree.print_helper(root)
