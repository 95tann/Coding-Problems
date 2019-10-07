''' 
Topic   : Binary Trees
Problem : Lowest Common Ancestor
Link    : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    if root == None:
        return None
    
    if root==p or root==q:
        return root
    
    lc = lowestCommonAncestor(root.left,p,q)
    rc = lowestCommonAncestor(root.right,p,q)
    
    if lc and rc:
        return root
    
    elif lc==None and rc==None:
        return None
    
    elif lc==None:
        return rc
    
    else:
        return lc