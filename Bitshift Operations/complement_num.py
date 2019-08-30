"""
Topic   : Bitshift Operations
Problem : Complement Number
Link    : https://leetcode.com/problems/number-complement/
""" 

def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    complement = count = 0
   
    while(num):
        remainder = (num % 2)
        if remainder == 0: 
            complement += 2**count * 1
        else: 
            complement += 2**count * 0
        count += 1
        num >>= 1
    
    return complement