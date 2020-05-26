'''
For each element ii in a list, it finds the first element to its right which is greater than ii.
For any element that such a value does not exist, the answer is -1

list = [4, 6, 3, 2, 8, 1]
result = [6, 8, 8, 8, -1, -1]
'''
from Stacks import myStack


def nextGreaterElement(lst):
    s = myStack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        # if stack has elements:
        if not s.isEmpty():
            # While stack has elements
            # and current element is greater than top element
            # pop all elements
            while not s.isEmpty() and s.top() <= lst[i]:
                s.pop()
        # if stack has an element
        # Top element will be greater than ith element
        if not s.isEmpty():
            res[i] = s.top()
        # push in the current element in stack
        s.push(lst[i])
        print(lst[i], s.stackList, res)

    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res


nge = nextGreaterElement([4, 6, 3, 2, 8, 1, 9, 9, 9])
