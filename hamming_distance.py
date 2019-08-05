"""
Topic   : Bitshift Operations
Problem : Hamming Distance
Link    : https://leetcode.com/problems/hamming-distance/
""" 
import check

def hamming_distance(num1, num2):
	if num1 == num2:
		return 0

	count = 0
	while(num1 > 0 or num2 > 0):
		count += (num1 % 2) ^ (num2 % 2)
		num1 = num1 >> 1
		num2 = num2 >> 1
	return count

# tests
check.expect(1,(hamming_distance(1,0)))
check.expect(0,(hamming_distance(0,0))
check.expect(1,(hamming_distance(4,5))
check.expect(5,(hamming_distance(32,9))
check.expect(8,hamming_distance(32,63))
