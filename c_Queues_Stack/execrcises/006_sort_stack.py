from c_Queues_Stack.stacks import Stack

"""
Implement a function called sort_stack() which takes a stack and 
sorts all of its elements in ascending order 
such that when they are popped and printed, they come out in ascending order. 
So the element that was pushed last to the stack has to be the smallest.
"""


def sort_stack(stack):
    temp_stack = Stack()

    while stack.is_empty() is False:
        value = stack.pop()

        if temp_stack.peek() and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while temp_stack.is_empty() is False and value < temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(value)

    while temp_stack.is_empty() is False:
        stack.push(temp_stack.pop())

    return stack


def sort_stack_recursive(stack):
    if stack.is_empty() is False:
        # Pop the top element off the stack
        value = stack.pop()
        # Sort the remaining stack recursively
        sort_stack_recursive(stack)
        # Push the top element back into the sorted stack
        insert(stack, value)


def insert(stack, value):
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(42)
    stack.push(12)
    stack.push(60)
    stack.push(23)

    # Sorting the stack
    stack = sort_stack(stack)

    # Printing the sorted stack
    print("Stack after sorting")
    print([stack.pop() for i in range(stack.size())])
