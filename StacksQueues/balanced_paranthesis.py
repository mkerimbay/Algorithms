'''
string containing only curly {}, square [], and round () parentheses. The function will tell us whether all the parentheses in the string are balanced or not.

For all the parentheses to be balanced, every opening parenthesis must have a closing one.
The order in which they appear also matters. For example, {[]} is balanced, but {[}] is not.


'''

from Stacks import myStack

def balanced_paranthesis(s):
    closing = ['}', ')', ']']
    stack = myStack()
    for character in exp:
        if character in closing:
            if stack.isEmpty():
                return False
            topElement = stack.pop()
            if (character is '}' and topElement is not '{'):
                return False
            if (character is ')' and topElement is not '('):
                return False
            if (character is ']' and topElement is not '['):
                return False
        else:
            stack.push(character)
    if (stack.isEmpty() is False):
        return False
    return True






exp = "{(({})]}"

print(balanced_paranthesis(exp))