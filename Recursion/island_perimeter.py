'''
Topic   : Depth First Search
Problem : Island Perimeter
Link    : https://leetcode.com/problems/island-perimeter/
'''

def DFS(row,col,grid,num_rows,num_cols):
    if (row<0 or col<0 or row>=num_rows or col>=num_cols):
        return 1
    
    if (grid[row][col]==0):
        return 1
    
    if (grid[row][col]=='X'):
        return 0
    
    if (grid[row][col]==1):
        grid[row][col]='X'
        up = DFS(row-1,col,grid,num_rows,num_cols)
        down = DFS(row+1,col,grid,num_rows,num_cols)
        left = DFS(row,col-1,grid,num_rows,num_cols)
        right = DFS(row,col+1,grid,num_rows,num_cols)
        return up+down+left+right


def islandPerimeter(grid):       
    perimeter = 0
    num_rows, num_cols = len(grid), len(grid[0])
    
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col]==1:
                perimeter = DFS(row,col,grid,num_rows,num_cols)
                break
    
    return perimeter