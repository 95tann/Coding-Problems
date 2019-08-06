''' 
Topic   : Dynamic Programming
Problem : Unique Paths 
Link    : https://leetcode.com/problems/unique-paths/
'''
def uniquePaths(m, n):
    matrix = [[1] * m for i in range(n)]
 
    for row in range(n):
        for col in range(m):
            if row != 0 and col != 0:
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
    
    return matrix[n-1][m-1]