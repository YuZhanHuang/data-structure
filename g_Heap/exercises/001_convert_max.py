"""
Implement a function convertMax(max_heap) which will convert a binary Max-Heap into a binary Min-Heap.
Where max_heap is a list which is given in the max_heap format, i.e, the parent is greater than its children.
"""


def min_heapify(heap, index):
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index
    # check if left child exists and is less than smallest
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left

    # check if right child exists and is less than smallest
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right

    # check if current index is not the smallest
    if smallest != index:
        # swap current index value with smallest
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        # minHeapify the new node
        min_heapify(heap, smallest)
    return heap


def convertMax(max_heap):
    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range((len(max_heap)) // 2, -1, -1):
        # call minHeapify on all parent nodes
        max_heap = min_heapify(max_heap, i)
    return max_heap


if __name__ == '__main__':
    max_heap_ = [9, 4, 7, 1, -2, 6, 5]
    print(convertMax(max_heap_))
