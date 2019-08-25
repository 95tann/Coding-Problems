'''
Topic   : Depth First Search
Problem : Word Search
Link    : https://leetcode.com/problems/word-search/
'''

def DFS(row,col,board,word,count):
    if count==len(word):
        return True
    elif (row>=len(board) or row<0 or col<0 or col>=len(board[0])):
        return False
    elif board[row][col] != word[count]:
        return False
    else:
        temp = board[row][col]
        board[row][col] = None
    
        up = DFS(row-1,col,board,word,count+1)
        down = DFS(row+1,col,board,word,count+1)
        left = DFS(row,col-1,board,word,count+1)
        right = DFS(row,col+1,board,word,count+1)
        
        board[row][col] = temp
        return left or right or up or down
        
def exist(board, word):
    num_rows, num_cols = len(board), len(board[0])
    
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col]==word[0] and DFS(row,col,board,word,0):
                return True                     
    
    return False
