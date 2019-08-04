''' 
Topic   : Edit/Levenstein Distance
Problem : https://leetcode.com/problems/edit-distance/
'''
import check

def levenstein_distance(str1, str2):
	len_str1 = len(str1)
	len_str2 = len(str2)

	matrix = []
	for i in range(len_str2+1):
		matrix.append([0]*(len_str1+1))

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
print(check.expect(3,(levenstein_distance('abc',''))))
print(check.expect(0,(levenstein_distance('hello','hello'))))
print(check.expect(2,(levenstein_distance('ham','ame'))))
print(check.expect(3,(levenstein_distance('horse','ros'))))