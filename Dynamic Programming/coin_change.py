'''
Topic   : Dynamic Programming
Problem : Coin Change
Link    : https://leetcode.com/problems/coin-change/
'''

def coinChange(coins, amount):           
    change = [amount+1] * (amount+1)
    change[0] = 0
    
    for i in range(1, amount+1):
        for denomination in coins:
            if denomination <= i:
                change[i] = min(change[i], 1+change[i-denomination])
                
    return -1 if change[-1]==amount+1 else change[-1]