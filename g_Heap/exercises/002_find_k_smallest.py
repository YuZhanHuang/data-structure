from g_Heap.min_heap import MinHeap

"""
Implement a function findKSmallest(lst,k) that takes an unsorted integer list as input and returns 
the “k” smallest elements in the list using a Heap. 
The minHeap class that was written in Min Heap (Implementation) is prepended to this exercise so feel free to use it! 
Have a look at the illustration given for a clearer picture of the problem
"""


def findKSmallest(lst, k):  # noqa
    min_heap = MinHeap()
    min_heap.buildHeap(lst)
    result = []

    for _ in range(k):
        result.append(min_heap.removeMin())

    return result


if __name__ == '__main__':
    lst = [9, 4, 7, 1, -2, 6, 5]
    k = 3
    print(findKSmallest(lst, k))
