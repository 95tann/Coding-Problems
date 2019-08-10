'''
Topic   : Arrays
Problem : Rotate Array
Link    : https://leetcode.com/problems/rotate-array/
'''
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if (k == 0) or (k % len(nums) == 0):
        return
            
    k = k % len(nums)
    nums[:k], nums[k:] = nums[-k:], nums[:-k]