"""
Find Two Numbers that Add up to "k"

In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and
return two numbers that add up to k.
In case there is more than one pair in the array containing numbers that add up to k,
you are required to return only one such pair. If no such pair is found then return an empty list.
"""


def find_sum(lst, k):
    tmp = {}

    for i in range(len(lst)):
        left = k - lst[i]
        tmp[lst[i]] = i
        if tmp.get(left):
            return [left, lst[i]] if lst[i] > left else [lst[i], left]

    return []


def binary_search(arr, item):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > item:
            left = mid + 1

        elif arr[mid] < item:
            right = mid - 1
        else:
            return mid


def find_sum_v2(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index != -1 and index != j:
            return [lst[j], k - lst[j]]


if __name__ == '__main__':
    print(find_sum([1, 2, 3, 4], 5))
    print(find_sum([1, 2, 3, 4], 2))