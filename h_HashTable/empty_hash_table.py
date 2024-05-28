from typing import List, Union


class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.nxt = None

    def __str__(self):
        return str(self.key) + ", " + self.value


class HashTable:
    # Constructor
    def __init__(self, slots=10, threshold=0.6):
        self.slots = slots
        self.size = 0
        self.bucket: Union[List[HashEntry], List[None]] = [None] * self.slots
        self.threshold = threshold

    # Helper Functions
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        ...

    def resize(self):
        ...

    def insert(self, key, value):
        ...

    # Return a value for a given key
    def search(self, key):
        ...

    # Remove a value based on a key
    def delete(self, key):
        ...


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
