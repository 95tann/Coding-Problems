'''
Topic   : Arrays
Problem : Jump Game
Link    : https://leetcode.com/problems/jump-game/
'''
def canJump(self, nums: List[int]) -> bool:
    curr_max = nums[0]
    
    for i in range(0,len(nums)):
        if i > curr_max:
            return False
        
        if curr_max >= len(nums)-1:
            return True
        
        if nums[i]+i > curr_max:
            curr_max = i + nums[i]