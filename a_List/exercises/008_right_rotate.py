"""
Implement a function right_rotate(lst, k) which will rotate the given list by k.
This means that the right-most elements will appear at the left-most position in the list and so on.
ou only have to rotate the list by one element at a time.
"""


def right_rotate(lst, k):
    if k == 0 or len(lst) == 0 or k == len(lst):
        return lst

    k = k % len(lst)
    leftover = len(lst) - k

    return lst[-k:] + lst[:leftover]


def right_rotate_v2(lst, k):
    if len(lst) == 0:
        return lst
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


if __name__ == '__main__':
    print(right_rotate([10, 20, 30, 40, 50], 3))
    print(right_rotate([], 1))
    print(right_rotate([1, 2, 3, 4, 5], 2))
    print(right_rotate([300, -1, 3, 0], 3))
    print(right_rotate([0, 0, 0, 2], 2))
    print(right_rotate(['13', 'a', 'Python'], 3))
    print(right_rotate(['right', 'rotate', 'python'], 4))

    print('========== version 2 ==========')
    print(right_rotate_v2([10, 20, 30, 40, 50], 3))
    print(right_rotate_v2([], 1))
    print(right_rotate_v2([1, 2, 3, 4, 5], 2))
    print(right_rotate_v2([300, -1, 3, 0], 3))
    print(right_rotate_v2([0, 0, 0, 2], 2))
    print(right_rotate_v2(['13', 'a', 'Python'], 3))
    print(right_rotate_v2(['right', 'rotate', 'python'], 4))
