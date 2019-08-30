'''
Topic   : Dynamic Programming
Problem : Arrange Coins
Link    : https://leetcode.com/problems/arranging-coins/
'''

# Solution 1
def arrangeCoins(n):        
    num_stairs = int(((1+8*n)**0.5 - 1)/2)
    return num_stairs     
    
# Solution 2
def arrangeCoins(n):  
    n -= 1
    num_stairs = 1
    staircase = [1]

    while(n >= (staircase[-1]+1)):
        staircase.append(staircase[-1]+1)
        n -= staircase[-1]
        num_stairs += 1

    return num_stairs