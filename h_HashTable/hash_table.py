from typing import List, Union


class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(self.key) + ", " + self.value


class HashTable:
    # Constructor
    def __init__(self, slots=10, threshold=0.6):
        # Size of the HashTable
        self.slots = slots
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket: Union[List[HashEntry], List[None]] = [None] * self.slots
        self.threshold = threshold

    # Helper Functions
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        # hash is a builtin function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket: Union[List[HashEntry], List[None]] = [None] * new_slots
        # rehash all items into new slots
        for item in self.bucket:
            head = item
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            # node = None
                            break
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            # node = None
                            break
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        if head is None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size += 1
        else:
            while head is not None:
                # 同一個slot裡面會有多個HashEntry Object
                # 插入同樣的key不一樣的值，會覆蓋原來的值
                if head.key is key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= self.threshold:
            self.resize()

    # Return a value for a given key
    def search(self, key):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None

    # Remove a value based on a key
    def delete(self, key):
        # Find index
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If key exists at first slot
        # 是否考慮使用 == 代替 is
        if head.key is key:
            self.bucket[b_index] = head.nxt
            # Decrease the size by one
            self.size -= 1
            return head
        # Find the key in slots
        prev = None
        while head is not None:
            # If key exists
            # 是否考慮使用 == 代替 is
            if head.key is key:
                prev.nxt = head.nxt
                # Decrease the size by one
                self.size -= 1
                return head
            # Else keep moving in chain
            prev, head = head, head.nxt

        # If key does not exist
        return


if __name__ == '__main__':
    table = HashTable()  # Create a HashTable
    print(table.is_empty())
    table.insert("This", 1)
    table.insert("is", 2)
    table.insert("a", 3)
    table.insert("Test", 4)
    table.insert("Driver", 5)
    print("Table Size: " + str(table.get_size()))
    print("The value for 'is' key: " + str(table.search("is")))
    table.delete("is")
    table.delete("a")
    print("Table Size: " + str(table.get_size()))