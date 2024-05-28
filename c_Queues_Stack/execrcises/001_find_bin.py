"""
Implement a function find_bin(n) which will generate binary numbers from
1 till n in the form of a string using a queue.
"""

from c_Queues_Stack.queues import Queue


def find_bin(number):
    queue = Queue()
    result = []
    for i in range(1, number + 1):
        s = "{0:b}".format(i)
        print(f'enqueue {s}')
        queue.enqueue(s)

    while queue.is_empty() is False:
        result.append(queue.dequeue())

    return result


if __name__ == '__main__':
    print(find_bin(5))