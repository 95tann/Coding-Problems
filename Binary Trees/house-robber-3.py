''' 
Topic   : Binary Trees
Problem : House Robber III
Link    : https://leetcode.com/problems/house-robber-iii/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    loot = dict()
    
    def rob(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        if root in self.loot: return self.loot[root]
        
        evn_amt = root.val
        if root.left:
            evn_amt += self.rob(root.left.left)
            evn_amt += self.rob(root.left.right)
        
        if root.right:
            evn_amt += self.rob(root.right.left)
            evn_amt += self.rob(root.right.right)
        
        odd_amt = self.rob(root.left) + self.rob(root.right)
        
        max_amt = max(odd_amt, evn_amt)
        self.loot[root] = max_amt
        return max_amt