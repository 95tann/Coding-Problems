'''
Topic   : Depth First Search
Problem : Surrounded Regions
Link    : https://leetcode.com/problems/surrounded-regions/
'''
def DFS(row,col,board,visited,num_rows,num_cols,flip_flag):
    # if position is out-of-bounds
    if (row < 0 or col < 0 or row >= num_rows or col >= num_cols): return
    
    # if position is visited or position value is 'X'
    if (board[row][col]=='X' or visited[row][col]==1): return
    
    # checking borders (do not flip)
    if (flip_flag):
        board[row][col] = 'X'
    
    # mark position as visited and recurse
    visited[row][col] = 1
    DFS(row+1,col,board,visited,num_rows,num_cols,flip_flag)
    DFS(row-1,col,board,visited,num_rows,num_cols,flip_flag)
    DFS(row,col+1,board,visited,num_rows,num_cols,flip_flag)
    DFS(row,col-1,board,visited,num_rows,num_cols,flip_flag)    


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if board==None or board==[]:
        return
    
    num_rows, num_cols = len(board), len(board[0])
    visited = [[0]*num_cols for i in range(num_rows)]
    
    # check borders
    for col in range(num_cols):
        if board[0][col]=='O' and visited[0][col]==0:
            DFS(0,col,board,visited,num_rows,num_cols,False)
        
        if board[num_rows-1][col]=='O' and visited[num_rows-1][col]==0:
            DFS(num_rows-1,col,board,visited, num_rows,num_cols,False)
    
    for row in range(num_rows):
        if board[row][0]=='O' and visited[row][0]==0:
            DFS(row,0,board,visited,num_rows,num_cols,False)
        
        if board[row][num_cols-1]=='O' and visited[row][num_cols-1]==0:
            DFS(row,num_cols-1,board,visited,num_rows,num_cols,False)
    
    # check for surrounded regions and flip 'O's to 'X's
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col]=='O' and visited[row][col]==0:
                DFS(row,col,board,visited,num_rows,num_cols,True)