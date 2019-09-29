''' 
Topic   : Dynamic Programming
Problem : Maximal Square
Link    : https://leetcode.com/problems/maximal-square/
'''   

def maximalSquare(matrix):
    if matrix == []: return 0
    
    num_rows, num_cols = len(matrix), len(matrix[0])
    dp = [[1 if matrix[row][col]=='1' else 0 for col in range(num_cols)] for row in range(num_rows)]
    
    for row in range(1,num_rows):
        for col in range(1,num_cols):
            if matrix[row][col]=='1':
                dp[row][col] = 1 + min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])
            
    max_area = 0
    for row in dp:
        max_area = max(max_area, max(row)**2)
    
    return max_area