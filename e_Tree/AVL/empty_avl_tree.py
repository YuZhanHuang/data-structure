class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.key)


class AVLTree:
    def update_height(self, node):
        ...

    # Function to insert a node
    def insert_node(self, root, key):
        return

    # Function to delete a node
    def delete_node(self, root, key):
        ...

    # Function to perform left rotation
    def left_rotate(self, z):
        ...

    # Function to perform right rotation
    def right_rotate(self, z):
        ...

    # Get the height of the node
    @staticmethod
    def get_height(node):
        ...

    # Get balance factor of the node
    def get_balance(self, node):
        ...

    def get_min_value_node(self, node):
        ...

    def pre_order(self, node):
        ...

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
