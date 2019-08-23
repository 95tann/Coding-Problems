'''
Topic   : Arrays
Problem : Set Matrix Zeroes
Link    : https://leetcode.com/problems/set-matrix-zeroes/
'''

# Solution 1
def setZeroes(matrix):
    zero_col, zero_row = [], []
    num_cols, num_rows = len(matrix[0]), len(matrix)
    
    for row in range(num_rows):
        for col in range(num_cols):
            if row not in zero_row or col not in zero_col:
                if matrix[row][col] == 0:
                    zero_col.append(col)
                    zero_row.append(row)
    
    for row in range(num_rows):
        for col in range(num_cols):
            if col in zero_col or row in zero_row:
                matrix[row][col] = 0


# Solution 2
def setZeroes(matrix):
	num_cols, num_rows = len(matrix[0]), len(matrix)
    set_col_1, set_row_1 = False, False
    
    for row in range(num_rows):
        for col in range(num_cols):
            if (matrix[row][col] == 0):
                if col == 0 and row == 0:
                    set_col_1 = True
                    set_row_1 = True
                
                elif col == 0 and row != 0:
                    set_col_1 = True
                
                elif col != 0 and row == 0:
                    set_row_1 = True
                
                else:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
           
    for row in range(1, num_rows):
        if matrix[row][0] == 0:
            for col in range(1, num_cols):
                matrix[row][col] = 0
    
    for col in range(1,num_cols):
        if matrix[0][col] == 0:
            for row in range(1, num_rows):
                matrix[row][col] = 0

    if set_row_1:
        for col in range(num_cols):
            matrix[0][col] = 0
   
    if set_col_1:
        for row in range(num_rows):
            matrix[row][0] = 0