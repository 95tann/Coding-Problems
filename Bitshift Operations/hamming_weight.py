"""
Topic   : Bitshift Operations
Problem : Hamming Weight
Link    : https://leetcode.com/problems/number-of-1-bits/
""" 

# Solution 1
############
def hammingWeight(n):
	return len(filter(lambda bit: bit == '1', str(bin(n))))


# Solution 2
############
def hammingWeight(n):
    weight = 0
    
    while(n):
        weight = weight if (n % 2 == 0) else weight+1
        n = n >> 1
    
    return weight