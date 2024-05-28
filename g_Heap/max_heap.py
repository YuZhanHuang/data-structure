class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            max_ = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max_
        elif len(self.heap) == 1:
            max_ = self.heap[0]
            del self.heap[0]
            return max_
        else:
            return None

    def __percolateUp(self, index):
        """
        This function will swap the values at parent-child nodes until the heap property is restored.
        :param index:
        :return:
        """
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        """
        This function restores the heap property after a node is removed.
        :param index:
        :return:
        """
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)

    def print_heap(self):
        print(self.heap)


if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)

    print(heap.getMax())
    heap.print_heap()

    heap2 = MaxHeap()
    heap2.buildHeap([1, 4, 5, 9, 10, 13, 3, 56])
    heap2.print_heap()

    while heap2.heap:
        print(heap2.removeMax())
