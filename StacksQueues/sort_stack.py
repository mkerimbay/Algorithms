'''takes a stack and sorts all of its elements in ascending order such that
when they are popped and printed, they come out in ascending order

stack = [23, 60, 12, 42, 4, 97, 2]

result = [97, 60, 42, 23, 12, 4, 2]
'''

from Stacks import myStack

def sort_stack(stack):
    tmp_stack = myStack()

    while not stack.isEmpty():
        value = stack.pop()
        if tmp_stack.top() is None or value >= tmp_stack.top():
            tmp_stack.push(value)
        else:
            while not tmp_stack.isEmpty():
                stack.push(tmp_stack.pop())
            stack.push(value)
        # print(stack.stackList, tmp_stack.stackList)
    while not tmp_stack.isEmpty():
        stack.push(tmp_stack.pop())
    return stack







stack = myStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(6)
stack.push(5)
print(stack.stackList)

stack = sort_stack(stack)
print(stack.stackList)