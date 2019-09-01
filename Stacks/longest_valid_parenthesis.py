'''
Topic   : Stacks
Problem : Longest Valid Parentheses
Link    : https://leetcode.com/problems/longest-valid-parentheses/
'''
def longestValidParentheses(s):
    if s == '': return 0
    
    stack = []
    max_length = 0
    
    for i, char in enumerate(s):
        if stack and char==')' and s[stack[-1]]=='(':
            stack.pop()
            max_length = max(max_length,i-stack[-1]) if stack else max(max_length,i+1)
        else:
            stack.append(i)
            
    return max_length