"""
Topic   : Arrays
Problem : Majority Element
Link    : https://leetcode.com/problems/majority-element/
""" 
def majorityElement(nums): 
	return sorted(nums)[len(nums)//2]