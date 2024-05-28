"""
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list
such that the 0th index will have the largest number, the 1st index will have the smallest,
and the 2nd index will have second-largest, and so on. In other words,
all the even-numbered indices will have the largest numbers in the list in
descending order and the odd-numbered indices will have the smallest numbers in ascending order.
"""
from typing import List


def max_min(lst: List[int]):
    """
    :param lst: ascending list,
    :return:
    """
    if not lst:
        return lst
    left, right = 0, len(lst) - 1
    result = []

    while left <= right:
        if left == right:
            result.append(lst[right])
        else:
            result.append(lst[right])
            result.append(lst[left])

        right -= 1
        left += 1

    return result


# 若全部為正整數此法可行
def max_min_v2(lst):
    if not lst:
        return lst

    max_index = len(lst) - 1  # max index
    min_index = 0  # first index
    max_element = lst[-1] + 1  # Max element

    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[max_index] % max_element) * max_element
            max_index -= 1
        # odd number means min number
        else:
            lst[i] += (lst[min_index] % max_element) * max_element
            min_index += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // max_element

    return lst


if __name__ == '__main__':
    print(max_min([1, 2, 3, 4, 5, 6, 7]))
    print(max_min([1, 2, 3, 4, 5]))
    print(max_min([]))
    print(max_min([1, 1, 1, 1, 1]))
    print(max_min([-10, -1, 1, 1, 1, 1]))

    print("========== version 2 ==========")
    print(max_min_v2([1, 2, 3, 4, 5, 6, 7]))
    print(max_min_v2([1, 2, 3, 4, 5]))
    print(max_min_v2([]))
    print(max_min_v2([1, 1, 1, 1, 1]))
    print(max_min_v2([-10, -1, 1, 1, 1, 1]))
