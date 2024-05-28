"""
Remove Even Integers from List

Implement a function that removes all the even elements from a given list. Name it remove_even(lst).
"""


def remove_even(lst):
    return [n for n in lst if n % 2 != 0]


if __name__ == '__main__':
    print(remove_even([3, 2, 41, 3, 34]))
