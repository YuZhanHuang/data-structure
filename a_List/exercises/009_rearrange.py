"""
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear
on the left and positive elements appear at the right of the list.
Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge!
So, zero will be placed at the right.
"""


def rearrange(lst):
    left = []
    right = []
    for l in lst:
        if l >= 0:
            right.append(l)
        else:
            left.append(l)

    return left + right


def rearrange_v2(lst):
    """
    rearrange in place
    :param lst:
    :return:
    """
    left_most_ele = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != left_most_ele:
                # swap the two
                lst[curr], lst[left_most_ele] = lst[left_most_ele], lst[curr]
            # update the last position
            left_most_ele += 1

    return lst


def rearrange_v3(lst):
    left_most_index = 0

    for i in range(len(lst)):
        if i == 0 and lst[i] < 0:
            continue

        if lst[i] < 0:
            lst[i], lst[left_most_index] = lst[left_most_index], lst[i]
            left_most_index += 1

    return lst


if __name__ == '__main__':
    print(rearrange_v2([-1, 2, -3, -4, 5]))
    print(rearrange_v2([300, -1, 3, 0]))
    print(rearrange_v2([0, 0, 0, -2]))
    print(rearrange_v3([-1, 2, -3, -4, 5]))