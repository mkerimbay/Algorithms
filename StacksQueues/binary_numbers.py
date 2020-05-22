'''
generate binary numbers from 1 to n in the form of a string
'''
from Queues import myQueue

def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        print('result', result)
        s1 = result[i] + "0"
        print('s1', s1)
        s2 = result[i] + "1"
        print('s2', s2)
        queue.enqueue(s1)
        queue.enqueue(s2)
        print(queue.queueList)

    return result  # For number = 3 , result = {"1","10","11"}


print(findBin(3))