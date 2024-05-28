from g_Heap.max_heap import MaxHeap


def findKLargest(lst, k):  # noqa
    max_heap = MaxHeap()
    max_heap.buildHeap(lst)
    result = []

    for _ in range(k):
        result.append(max_heap.removeMax())

    return result


if __name__ == '__main__':
    lst = [9, 4, 7, 1, -2, 6, 5]
    k = 3
    print(findKLargest(lst, k))