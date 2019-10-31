'''
Topic   : Binary Trees
Problem : Minimum Depth of Binary Tree
Link    : https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def minDepth(root)
      if root == None:
          return 0

      lc, rc = root.left, root.right

      if lc and rc:
          return 1 + min(self.minDepth(lc), self.minDepth(rc))
      elif lc:
          return 1 + minDepth(lc)
      elif rc: 
          return 1 + minDepth(rc)
      else:
          return 1
