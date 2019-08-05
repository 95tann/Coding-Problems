''' 
Topic   : Dynamic Programming
Problem : House Robber
Link    : https://leetcode.com/problems/house-robber/
'''
def rob(nums):
    houses = len(num)
    if houses == 0:
        return 0
    
    max_stolen = [0]*houses
    
    for i, num in enumerate(nums):
        if i == 0:
            max_stolen[i] = num
        elif i == 1:
            max_stolen[i] = max(num,max_stolen[0])
        else:
            max_stolen[i] = max(max_stolen[i-1], num+max_stolen[i-2])
            
    return max_stolen[-1]