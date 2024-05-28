class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        ...

    def get_min(self):
        ...

    def remove_min(self):
        ...

    def __percolate_up(self, idx):
        ...

    def __min_heapify(self, idx):
        ...

    def build_heap(self, arr):
        ...

    def print_heap(self):
        print(self.heap)


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)

    print(heap.get_min())
    heap.print_heap()

    heap2 = MinHeap()
    heap2.build_heap([1, 4, 5, 9, 10, 13, 3, 56])
    heap2.print_heap()

    while heap2.heap:
        print(heap2.remove_min())
