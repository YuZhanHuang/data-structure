"""
Merge Two Sorted Lists

Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
 Name it merge_lists(lst1, lst2).
"""


def merge_lists(lst1, lst2):
    ptr_1, ptr_2 = 0, 0
    result = []

    while ptr_1 < len(lst1) and ptr_2 < len(lst2):
        if lst1[ptr_1] <= lst2[ptr_2]:
            result.append(lst1[ptr_1])
            ptr_1 += 1
        else:
            result.append(lst2[ptr_2])
            ptr_2 += 1

    if ptr_2 < len(lst2):
        result.extend(lst2[ptr_2:])

    if ptr_1 < len(lst1):
        result += lst1[ptr_1:]

    return result


if __name__ == '__main__':
    a_list = [1, 4, 5, 7]
    b_list = [3, 9, 12, 19]
    print(merge_lists(a_list, b_list))
