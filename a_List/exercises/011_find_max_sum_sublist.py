"""
Given an unsorted list A, the maximum sum sub list is the sub list (contiguous elements) from
A for which the sum of the elements is maximum. In this challenge,
we want to find the sum of the maximum sum sub list.
This problem is a tricky one because the list might have negative integers in any position,
so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.
"""


def find_max_sum_sublist_brute_force(lst):
    max_sum = float('-inf')  # Start with the smallest possible value

    # Check if the list is empty
    if not lst:
        return 0

    # Outer loop goes through each element
    for start_index in range(len(lst)):
        # Inner loop considers all sublists starting from start_index
        for end_index in range(start_index + 1, len(lst) + 1):
            # Calculate the sum of the current sublist
            current_sum = sum(lst[start_index:end_index])
            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


def find_max_sum_sublist(lst):
    """
    Kadane’s Algorithm
    :param lst:
    :return:
    """
    curr_max, global_max = lst[0], lst[0]
    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]

        if global_max < curr_max:
            global_max = curr_max

    return global_max


if __name__ == '__main__':
    print(find_max_sum_sublist([2, 3, -1, 4, -6]))
