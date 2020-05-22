'''
reverse first k elements in queue
'''

from Stacks import myStack
from Queues import myQueue

def reverseK(queue, k):
    if queue.isEmpty() or queue.size() < k or k < 0:
        return None
    n = queue.size()

    stack = myStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while not stack.isEmpty():
        queue.enqueue(stack.pop())

    for i in range(n-k):
        queue.enqueue(queue.dequeue())

    return queue


queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)

print(queue.queueList)

queue = reverseK(queue, 5)
print(queue.queueList)

