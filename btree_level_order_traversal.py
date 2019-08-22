'''
Topic   : Binary Trees
Problem : Level Order Traversal
Link    : https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def levelOrder(root):
    if root == None:
        return []
    
    level_order = []
    level_order.append([root.val])
    q = [root]       

    while(q):
        next_level_nodes, next_level_val = [], []
        for node in q:
            lc, rc = node.left, node.right

            if lc:
                next_level_nodes.append(lc)
                next_level_val.append(lc.val)
            if rc:
                next_level_nodes.append(rc)
                next_level_val.append(rc.val)

        if next_level_val: level_order.append(next_level_val)
        q = next_level_nodes

    return level_order