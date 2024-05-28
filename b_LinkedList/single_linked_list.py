class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, data):
        node = Node(data)
        head = self.head_node

        while head.next_element is not None:
            head = head.next_element

        head.next_element = node

        return node

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        if self.is_empty():
            return

        first_element = self.head_node
        self.head_node, first_element.next_element = first_element.next_element, None

        return

    def delete_at_tail(self):
        if self.is_empty():
            return

        head = self.head_node
        prev = None

        while head.next_element is not None:
            prev = head
            head = head.next_element

        prev.next_element = None

        return head

    def delete_by_value(self, data):
        head = self.head_node
        prev = None
        if self.is_empty():
            return

        if head.data == data:
            return self.delete_at_head()

        while head.next_element is not None:
            if head.data == data:
                break
            prev, head = head, head.next_element

        prev.next_element = head.next_element

        return head

    def search(self, data):
        head = self.head_node

        while head is not None:
            if head.data == data:
                return True, head.data

            head = head.next_element

        return False, None

    def length(self):
        count = 0
        head = self.head_node
        if self.is_empty():
            return count

        while head is not None:
            count += 1
            head = head.next_element

        return count

    def middle_node(self):
        slow, fast = self.head_node, self.head_node

        while fast and fast.next_element:
            slow = slow.next_element
            fast = fast.next_element.next_element

        return slow.data

    def middle_node_v2(self):
        if self.is_empty():
            return None

        node = self.head_node
        if self.length() % 2 == 0:
            mid = self.length() // 2
        else:
            mid = self.length() // 2 + 1

        for _ in range(mid - 1):
            node = node.next_element

        return node.data

    def find_duplicate(self):
        seen = set()
        head = self.head_node
        prev = None

        while head is not None:
            if head.data not in seen:
                seen.add(head.data)
                prev = head
                head = head.next_element
            else:
                while head in seen:
                    head = head.next_element
                    if head is None:
                        break
                prev.next_element = head

    # Exercises
    def n_node_from_end(self, n):
        """
        倒數第n個node
        :param n:
        :return:
        """
        head = self.get_head()
        if not head:
            return

        left, right = head, head

        for _ in range(n):
            right = right.next_element
            if right is None:
                return None

        while right is not None:
            left = left.next_element
            right = right.next_element

        return left.data

    def remove_duplicates(self):
        if self.is_empty():
            return

        current_node = self.get_head()
        prev_node = self.get_head()
        # To store values of nodes which we already visited
        visited_nodes = set()
        # If List is not empty and there is more than 1 element in List
        if not self.is_empty() and current_node.next_element:
            while current_node:
                value = current_node.data
                if value in visited_nodes:
                    # current_node is already in the HashSet
                    # connect prev_node with current_node's next element
                    # to remove it
                    prev_node.next_element = current_node.next_element
                    current_node = current_node.next_element
                    continue
                # Visiting currentNode for first time
                visited_nodes.add(current_node.data)
                prev_node = current_node
                current_node = current_node.next_element
        return

    def remove_duplicates_v2(self):
        if self.head_node:
            return

        head = self.get_head()
        prev = None
        seen = set()

        while head is not None:
            if head.data not in seen:
                seen.add(head.data)
                prev = head
                head = head.next_element
            else:
                while head.data in seen:
                    head = head.next_element
                    if head is None:
                        break
                prev.next_element = head

        return self.get_head()


if __name__ == '__main__':
    sll = LinkedList()
    for i in range(11):
        sll.insert_at_head(i)

    sll.print_list()

    sll.delete_at_head()
    sll.delete_at_head()

    print('Delete head node twice.')
    sll.print_list()

    print('Insert -1, -2 at tail')
    sll.insert_at_tail(-1)
    sll.insert_at_tail(-2)

    sll.print_list()

    print('Delete tail node once')
    sll.delete_at_tail()
    sll.print_list()

    print('Search 8 in linked list', sll.search(8))
    print('Search 9 in linked list', sll.search(9))
    print('Search 7 in linked list', sll.search(7))
    print('Search 4 in linked list', sll.search(4))
    print('Search 0 in linked list', sll.search(0))
    print('Search -1 in linked list', sll.search(-1))
    print('Search None in linked list', sll.search(None))

    print('Delete by value 3')
    sll.delete_by_value(3)
    sll.print_list()

    print('Total Nodes', sll.length())
    print('Find middle node', sll.middle_node())
