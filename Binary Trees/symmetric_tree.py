'''
Topic   : Binary Trees
Problem : Symmetric Tree
Link    : https://leetcode.com/problems/symmetric-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#  

def traverse(t1,t2):
    if t1==None and t2==None: 
    	return True

    if t1 and t2:
        if t1.val != t2.val:
            return False
        else:
            return traverse(t1.left,t2.right) and traverse(t1.right, t2.left)
        
   	return False

def isSymmetric(root):
    return True if not root else traverse(root.left,root.right)