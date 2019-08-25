'''
Topic   : Binary Trees
Problem : Same Binary Trees
Link    : https://leetcode.com/problems/same-tree/
'''
def isSameTree(p,q):
    if p and q:
        if p.val == q.val:
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        else:
            return False
        
    elif p==None and q==None:
        return True
    
    else:
        return False