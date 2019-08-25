'''
Topic   : Binary Trees
Problem : Path Sum
Link    : https://leetcode.com/problems/path-sum/
'''

# Solution 1
def hasPathSum(root,target):
    if not root:
        return False

    if not root.left and not root.right:
        return True if (root.val - target == 0) else False
     
    left = hasPathSum(root.left, target - root.val)
    right = hasPathSum(root.right, target - root.val)
    return left or right


# Solution 2
def traverse(node,target,sum_so_far):
    lc, rc = node.left, node.right
    left_subtree, right_subtree = None,None
    
    if lc==None and rc==None:
        return True if sum_so_far+node.val==target else False

    if lc:
        left_subtree = traverse(node.left,target,sum_so_far + node.val)
    
    if rc:
        right_subtree = traverse(node.right,target,sum_so_far + node.val)
    
    return left_subtree or right_subtree
    
def hasPathSum(root, target):
    return traverse(root,sum,0) if root else False