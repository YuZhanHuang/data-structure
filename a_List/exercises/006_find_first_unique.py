from collections import defaultdict

"""
First Non-Repeating Integer in a List

Implement a function, find_first_unique(lst) that returns the first unique integer in the list.
"""


def find_first_unique(lst):
    for index1 in range(len(lst)):
        index2 = 0

        while index2 < len(lst):
            if index1 != index2 and lst[index1] == lst[index2]:
                break
            index2 += 1
        if index2 == len(lst):
            return lst[index1]
    return None


def find_first_unique_v2(lst):
    counter = defaultdict(int)
    for element in lst:
        counter[str(element)] += 1

    for element in lst:
        counter[str(element)] -= 1
        if counter[str(element)] == 0:
            return element


if __name__ == '__main__':
    print(find_first_unique([9, 2, 3, 2, 6, 6]))  # 9
    print(find_first_unique_v2([9, 2, 3, 2, 6, 6]))  # 9
