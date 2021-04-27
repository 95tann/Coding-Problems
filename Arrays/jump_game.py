'''
Topic   : Arrays
Problem : Jump Game
Link    : https://leetcode.com/problems/jump-game/
'''
def canJump(self, nums: List[int]) -> bool:
    max_reachable = 0
        
    for i in range(len(nums)):
        if max_reachable < i:
            return False

        max_reachable = max(i+nums[i], max_reachable)

    return True
