'''
Topic   : Arrays
Problem : Max Product of 3 Numbers
Link    : https://leetcode.com/problems/maximum-product-of-three-numbers/
'''

def maximumProduct(nums):
    nums.sort()
    case1 = nums[-1] * nums[-2] * nums[-3]
    case2 = nums[-1] * nums[0] * nums[1]
    return max(case1,case2)