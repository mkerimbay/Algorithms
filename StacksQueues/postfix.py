from Stacks import myStack


def evaluatePostFix(exp):
    stack = myStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
                print(stack.stackList)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"


print("Result: " + str(evaluatePostFix("921*-8-4+")))
print("Result: " + str(evaluatePostFix("921*-8--4+")))
