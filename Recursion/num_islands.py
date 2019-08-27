'''
Topic   : Depth First Search
Problem : Number of Islands
Link    : https://leetcode.com/problems/number-of-islands/
'''

def DFS(row,col,grid, num_rows, num_cols):
    # went out-of-bounds:
    if (row < 0 or col < 0 or row >= num_rows or col >= num_cols): return 
    
    # current cell is 0
    if (grid[row][col] == '0'): return
    
    # current cell is already visited
    if (grid[row][col] == 'X'): return
    
    # recurse up, down, left, right
    grid[row][col] = 'X'
    DFS(row-1,col,grid,num_rows,num_cols)
    DFS(row+1,col,grid,num_rows,num_cols)
    DFS(row,col-1,grid,num_rows,num_cols)
    DFS(row,col+1,grid,num_rows,num_cols)    

def numIslands(grid):
    if grid==None or grid==[]:
        return 0
    
    num_islands = 0
    num_rows, num_cols = len(grid), len(grid[0])
    
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '1':
                num_islands += 1
                DFS(row,col,grid,num_rows,num_cols)
            
    return num_islands