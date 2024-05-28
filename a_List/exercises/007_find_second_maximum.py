"""
Implement a function find_second_maximum(lst) which returns the second-largest element in the list.
"""


def find_second_maximum(lst):
    first_max, second_max = float('-Infinity'), float('-Infinity')
    for l in lst:
        if l > first_max:
            second_max = first_max
            first_max = l
        elif l > second_max:
            second_max = l

    return second_max


if __name__ == '__main__':
    print(find_second_maximum([9, 2, 3, 6]))  # 6
    print(find_second_maximum([4, 2, 1, 5, 0]))  # 4