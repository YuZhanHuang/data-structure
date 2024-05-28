class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        ...

    def get_max(self):
        ...

    def remove_max(self):
        ...

    def __percolate_up(self, idx):
        ...

    def __max_heapify(self, idx):
        ...

    def build_heap(self, arr):
        ...

    def print_heap(self):
        print(self.heap)


if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)

    print(heap.get_max())
    heap.print_heap()

    heap2 = MaxHeap()
    heap2.build_heap([1, 4, 5, 9, 10, 13, 3, 56])
    heap2.print_heap()

    while heap2.heap:
        print(heap2.remove_max())
