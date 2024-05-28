from c_Queues_Stack.queues import Queue
from c_Queues_Stack.stacks import Stack

"""
Implement the following functions to implement two stacks using a single array such that for storing elements 
both stacks should use the same array.
Also, for this problem, initialize a Python list with the provided fixed size and perform all the operations 
in-place without growing or shrinking the list!

In case the value of “k” is larger than the size of the queue, is smaller than 0, or if the queue is empty, 
simply return None instead.
"""


def reverse_k(queue, k):
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())

    while stack.is_empty() is False:
        queue.enqueue(stack.pop())

    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    print("the queue before reversing:")
    print(q.items)
    reverse_k(q, 10)
    print("the queue after reversing:")
    print(q.items)
