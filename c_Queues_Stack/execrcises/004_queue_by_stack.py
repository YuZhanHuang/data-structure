from c_Queues_Stack.stacks import Stack

"""
You have to implement the enqueue() and dequeue() functions using the Stack class we created earlier.
 `enqueue()` will insert a value into the queue and `dequeue()` will remove a value from the queue.
"""


class QueueQuickOut:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())

            self.main_stack.push(value)

            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        if self.main_stack.is_empty():
            return
        return self.main_stack.pop()


class QueueQuickIn:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            return
        if self.temp_stack.is_empty() is False:
            return self.temp_stack.pop()

        while self.main_stack.is_empty() is False:
            self.temp_stack.push(self.main_stack.pop())

        return self.temp_stack.pop()


if __name__ == '__main__':
    print('========== Quick In Queue ==========')
    queue = QueueQuickIn()
    for i in range(5):
        print(f'enqueue: {i+1}')
        queue.enqueue(i + 1)
    print("----------")
    for i in range(5):
        popped = queue.dequeue()
        print(f'dequeue: {popped}')

    print('========== Quick Out Queue ==========')
    queue = QueueQuickOut()
    for i in range(5):
        print(f'enqueue: {i+1}')
        queue.enqueue(i + 1)
    print("----------")
    for i in range(5):
        popped = queue.dequeue()
        print(f'dequeue: {popped}')
