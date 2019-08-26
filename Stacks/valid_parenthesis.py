'''
Topic   : Stacks
Problem : Valid Parentheses
Link    : https://leetcode.com/problems/valid-parentheses/
'''
def isValid(s):
    stack = []
    for char in s:
        if char in ['(','{','[']:
            stack.append(char)
        else:
            if stack:
                popped = stack.pop()
                if popped == '(' and char != ')':
                    return False
                if popped == '{' and char != '}':
                    return False
                if popped == '[' and char != ']':
                    return False
            else:
                return False
            
    return False if stack else True