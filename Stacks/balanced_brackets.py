'''
Topic   : Stacks
Problem : Balanced Brackets
Link    : HackerRank
'''
def balancedOrNot(expressions, maxReplacements):
    result = []
    
    for exp, replacements in zip(expressions,maxReplacements):
        stack = []
        for char in exp:
            if char == "<":
                stack.append(char)
            else:
                if stack:
                    if stack[-1]=='<':
                        stack.pop()
                    else:
                        replacements -= 1
                        stack.pop()
                else:
                    replacements -= 1
        
        if stack: replacements = -1
        
        if replacements >= 0: result.append(1)
        else: result.append(0)
            
    return result 