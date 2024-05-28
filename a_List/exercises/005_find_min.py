"""
Find Minimum Value in List

Implement a function find_minimum(lst) which finds the smallest number in the given list.
"""


def find_minimum(arr):
    min_index = 0
    for i in range(len(arr)):
        if arr[i] <= arr[min_index]:
            min_index = i

    return arr[min_index]


if __name__ == '__main__':
    print(find_minimum([9, 2, 3, 6]))
