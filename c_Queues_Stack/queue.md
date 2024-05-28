## Type of Queues
- Linear Queue
- Circular Queue
- Priority Queue
- Double-ended Queue

### Linear Queue
### Circular Queue
Circular queues are almost similar to linear queues with only one exception. 
As the name itself suggests, circular queues are circular in structure which means that both ends are connected to form a circle. 
Initially, the front and rear part of the queue point to the same location. Eventually they move apart as more elements are inserted into the queue. 
Circular queues are generally used in:

- Simulation of objects
- Event handling (do something when a particular event occurs)

### Priority Queue
In priority queues, 
all elements have a priority associated with them and are sorted such that the most prioritized object appears 
at the front and the least prioritized object appears at the end of the queue. 
These queues are widely used in most operating systems to determine which programs should be given more priority.

### Double-ended Queue
The double-ended queue acts as a queue from both ends(back and front). 
It is a flexible data structure that provides enqueue and dequeue functionality on both ends in O(1). 
Hence, it can act like a normal linear queue if needed. 
Python has a built-in deque class that can be imported from the collections module. 
The class contains several useful methods such as rotate. 
Looking back, the **Right Rotate** List challenge can be solved easily with deque.rotate(). Try it out as a small exercise.

## Complexities of Queue Operations
| Operation | Complexity |
|-----------|------------|
| enqueue   | O(1)       |
| dequeue   | O(1)       |
| front     | O(1)       |
| rear      | O(1)       |
| size      | O(1)       |
| is_empty  | O(1)       |