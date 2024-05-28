from c_Queues_Stack.stacks import Stack

"""
You are required to implement the next_greater_element() function. For each element i in a list, 
the function finds the first element to its right which is greater than element i.
If for any element such a value does not exist, the answer is -1.

e.g.
list   = [4, 6, 3, 2,  8,  1]
result = [6, 8, 8, 8, -1, -1]
"""


# 從尾開始找
def next_greater_element(lst):
    stack = Stack()
    # 最後一個絕對不會有下一個比他大
    res = [-1] * len(lst)

    for i in range(len(lst) - 1, -1, -1):
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()

        if not stack.is_empty():
            res[i] = stack.peek()

        stack.push(lst[i])

    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))

    return res


if __name__ == '__main__':
    nge = next_greater_element([4, 6, 3, 2, 8, 1, 1000])
