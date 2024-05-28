from c_Queues_Stack.stacks import Stack


"""
You have to implement the MinStack class which will have a min() function. 
Whenever min() is called, the minimum value of the stack is returned in O(1) time. 
The element is not popped from the stack.
Its value is simply returned.
"""


class MinStack:
    def __init__(self):
        self.main_stack = Stack()
        self.min_stack = Stack()

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # KEY !!!
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    def min_value(self):
        return self.min_stack.peek() if not self.min_stack.is_empty() else None


if __name__ == '__main__':
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min_value()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min_value()))
    stack.pop()
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min_value()))
