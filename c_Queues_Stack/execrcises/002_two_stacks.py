"""
Implement the following functions to implement two stacks using a single array such that for storing elements
both stacks should use the same array.
Also, for this problem, initialize a Python list with the provided fixed size and perform all
the operations in-place without growing or shrinking the list!
"""


class TwoStacks:

    # constructor
    def __init__(self, n):
        self.size = n
        # populating 0s on all n indices of array arr
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element vale to stack1
    def push1(self, vale):
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = vale

        print("Stack Overflow ")

    # Method to push an element x to stack2
    def push2(self, vale):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = vale

        print("Stack Overflow ")

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            popped = self.arr[self.top1]
            self.arr[self.top1] = 0
            self.top1 -= 1
            return popped

        print("Stack Underflow ")

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            popped = self.arr[self.top2]
            self.arr[self.top2] = 0
            self.top2 += 1
            return popped
        print("Stack Underflow ")


if __name__ == "__main__":
    stack = TwoStacks(10)
    stack.push1(20)
    stack.push2(10)
    print(stack.arr)
    print(stack.pop1())
    print(stack.arr)
    stack.push1(100)
    print(stack.arr)
    print(stack.pop2())
    print(stack.arr)
