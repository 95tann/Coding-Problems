''' 
Topic   : Binary Trees
Problem : Lowest Common Ancestor
Link    : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    if root==None:
        return None
    
    if root.val <= max(p.val,q.val) and root.val >= min(p.val,q.val):
        return root
    
    elif max(p.val,q.val) < root.val:
        return lowestCommonAncestor(root.left,p,q)
        
    else:
        return lowestCommonAncestor(root.right,p,q)
