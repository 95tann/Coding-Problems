
''' 
Topic   : Binary Search Trees
Problem : Valid BST
Link    : https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees
''' 

def checkBST_helper(curr_node,min_val,max_val):
    '''
    class node:
        def __init__(self, data):
            self.data = data
            self .left = None
            self.right = None
    '''
    if curr_node.data>min_val and curr_node.data<max_val:
        
        if curr_node.left and curr_node.right:
            left_subtree = checkBST_helper(curr_node.left,min_val,curr_node.data)
            right_subtree = checkBST_helper(curr_node.right,curr_node.data,max_val)
            return True and left_subtree and right_subtree
        
        elif curr_node.left:
            return True and checkBST_helper(curr_node.left,min_val,curr_node.data)
        
        elif curr_node.right:
            return True and checkBST_helper(curr_node.right,curr_node.data,max_val)
        
        else:
            return True
    
    else:
        return False

def checkBST(root):
    if root == None:
        return False
    else:
        from sys import maxsize
        return checkBST_helper(root,1-maxsize,maxsize)