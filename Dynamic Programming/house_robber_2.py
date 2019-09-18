''' 
Topic   : Dynamic Programming
Problem : House Robber II
Link    : https://leetcode.com/problems/house-robber-ii/
'''

def rob(nums):
    len_nums = len(nums)
    
    # Base Cases
    if len_nums == 0: return 0
    if len_nums == 1: return nums[0]
    if len_nums == 2: return max(nums[0],nums[1])
    
    # First Pass
    pass1 = [0] * (len_nums-1)        
    pass1[0] = nums[0]
    pass1[1] = max(nums[0], nums[1])
    for i in range(2, len_nums-1):
        pass1[i] = max(nums[i]+pass1[i-2], pass1[i-1])
    
    # Second Pass
    pass2 = [0] * (len_nums-1)
    pass2[0] = nums[1]
    pass2[1] = max(nums[1], nums[2])
    for j in range(3, len_nums):
        pass2[j-1] = max(nums[j]+pass2[j-3], pass2[j-2])
    
    # Result
    return max(pass1[-1],pass2[-1])