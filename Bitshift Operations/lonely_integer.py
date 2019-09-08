'''
Topic   : Bitshift Operations
Problem : Lonely Integer
Link    : https://www.hackerrank.com/challenges/lonely-integer/problem
'''

def lonelyinteger(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor