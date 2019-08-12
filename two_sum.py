"""
Topic   : Arrays
Problem : Two Sum
Link    : https://leetcode.com/problems/two-sum/
""" 

def twoSum(nums, target):
    positions = {}
   
    for i, num in enumerate(nums):
        complement = target-num
        
        if complement in positions:
            return [positions[complement],i]
        
        positions[num] = i