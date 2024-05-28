class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if self.head is not None:
            return self.head.data
        else:
            return False

    def is_empty(self):
        if self.head is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, data):
        temp_node = Node(data)
        if self.is_empty():
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node

    def remove_head(self):
        if self.is_empty():
            return False
        node_to_remove = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node_to_remove.next_element
            self.head.previous_element = None
            node_to_remove.next_element = None

        self.length -= 1
        return node_to_remove.data

    def remove_by_value(self, value):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted

        current_node = self.get_head()
        if current_node.data == value:
            return self.remove_head()

        # Traversing/Searching for node to Delete
        while current_node:
            if current_node.data == value:
                break

            current_node = current_node.next_element

        current_node.previous_element.next_element = current_node.next_element
        self.length -= 1

        return current_node

    def tail_node(self):
        if self.head is not None:
            return self.tail.data
        else:
            return False

    def __str__(self):
        if self.is_empty():
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while temp.next_element:
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val