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


'''
Topic   : Arrays & Dynamic Programming
Problem : Jump Game II
Link    : https://leetcode.com/problems/jump-game-ii/
'''
def jump(self, nums: List[int]) -> int:
    min_jumps = [10**5 for i in range(len(nums))]
    min_jumps[0] = 0

    for i, num in enumerate(nums):
        for jump_size in range(num+1):
            if i+jump_size < len(nums):
                min_jumps[i+jump_size] = min(min_jumps[i+jump_size], 1+min_jumps[i])        

    return min_jumps[-1]
