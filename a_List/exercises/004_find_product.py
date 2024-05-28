from typing import List

"""
List of Products of all Elements

Implement a function, find_product(lst), which modifies a list so that each index has a product of 
all the numbers present in the list except the number stored at that index.
"""


def find_product(lst):
    product: List[int] = [-1] * len(lst)

    for i in range(len(lst)):
        multiplier = 1
        for j in range(len(lst)):
            if i == j:
                continue
            multiplier *= lst[j]

        product[i] = multiplier

    return product


def find_product_v2(lst):
    product = []
    left = 1

    for n in lst:
        product.append(left)
        left *= n

    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


if __name__ == '__main__':
    print(find_product([2, 5, 9, 3, 6]))
    print(find_product_v2([2, 5, 9, 3, 6]))
