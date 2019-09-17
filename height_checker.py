'''
Topic   : Arrays
Problem : Height Checker
Link    : https://leetcode.com/problems/height-checker/
'''

def heightChecker(heights):
    count = 0
    for num1, num2 in zip(heights, sorted(heights)):
        if num1 != num2:
            count += 1
    return count