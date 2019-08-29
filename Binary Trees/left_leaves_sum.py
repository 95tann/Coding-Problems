'''
Topic   : Binary Trees
Problem : Sum of Left Leaves
Link    : https://leetcode.com/problems/sum-of-left-leaves/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def traverse(self, node, is_left):        
    lc, rc = node.left, node.right
    
    if lc and rc: 
        return traverse(lc, True) + traverse(rc, False)
    elif lc: 
        return traverse(lc, True)
    elif rc: 
        return traverse(rc, False)
    else: 
        return node.val if is_left else 0            

def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if root==None: return 0
    
    lc, rc = root.left, root.right
    
    if lc and rc: 
        return traverse(lc, True) + traverse(rc, False)
    elif lc: 
        return traverse(lc, True)
    elif rc: 
        return traverse(rc, False)
    else: 
        return 0