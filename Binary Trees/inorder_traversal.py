''' 
Topic   : Binary Trees
Problem : Iterative In-order Traversal 
Link    : https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive Solution
def helper(node,lst):
    if node:
        helper(node.left,lst)
        lst.append(node.val)
        helper(node.right,lst)

def inorderTraversal(root):
    if root==None:
        return []
    
    result = []
    helper(root,result)
    return result


# Iterative Solution
def inorderTraversal(root):
    stack, result = [], []
    curr_node = root
        
    while(curr_node or stack):
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        
        else:
            popped = stack.pop()
            result.append(popped.val)
            curr_node = popped.right
    
    return result
