''' 
Topic   : Binary Trees
Problem : Iterative In-order Traversal 
Link    : https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

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