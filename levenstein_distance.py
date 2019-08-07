''' 
Topic   : Dynamic Programming
Problem : Edit/Levenstein Distance
Link    : https://leetcode.com/problems/edit-distance/
'''
from check import expect

def levenstein_distance(str1, str2):
	len_str1 = len(str1)
	len_str2 = len(str2)

	matrix = [[0]*(len_str1+1) for i in range(len_str2+1)]

	for row in range(len_str2 + 1):
		for col in range(len_str1 + 1):
			if row == 0:
				matrix[row][col] = col
			elif col == 0:
				matrix[row][0] = row
			else:
				if str2[row-1] == str1[col-1]:
					matrix[row][col] = matrix[row-1][col-1]
				else:
					matrix[row][col] = 1 + min(matrix[row][col-1],matrix[row-1][col],matrix[row-1][col-1])	
			
	#print(matrix)
	return matrix[len_str2][len_str1]

# Tests
print(expect(3,(levenstein_distance('abc',''))))
print(expect(0,(levenstein_distance('hello','hello'))))
print(expect(2,(levenstein_distance('ham','ame'))))
print(expect(3,(levenstein_distance('horse','ros'))))
print(expect(3,(levenstein_distance('honda','hyundai'))))
print(expect(2,(levenstein_distance('geely','gily'))))