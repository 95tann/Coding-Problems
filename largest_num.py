'''
Topic   : Strings
Problem : Largest Number
Link    : https://leetcode.com/problems/largest-number/
'''
from functools import cmp_to_key

def comparator(x,y):
    return 1 if x+y > y+x else -1

def largestNumber(nums):
    str_list = list(map(str, nums))
    str_list.sort(key=cmp_to_key(comparator), reverse=1)
    result = "".join(str_list)
    return result if result[0] != '0' else '0'