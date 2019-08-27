''' 
Topic   : Linked-List
Problem : Remove Nth Node
Link    : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Solution 1
def removeNthFromEnd(head, n)
    pointers = []
    while(head):
        pointers.append(head)
        head = head.next
    ll_length = len(pointers)
    
    if n == 0:
        return pointers[0]
    
    elif(ll_length == n):
        return None if ll_length==1 else pointers[1]
    
    elif(n == 1):
        pointers[-2].next = None
        return pointers[0]
    
    else:
        pointers[ll_length-n-1].next = pointers[ll_length-n+1]
        return pointers[0]


# Solution 2
def removeNthFromEnd(head, n):
    if n==0:
        return head
    
    start_ptr = end_ptr = head
    count = 0
    
    while(count != n):
        end_ptr = end_ptr.next
        if end_ptr == None and n==1: return None
        if end_ptr == None: return start_ptr.next   
        count += 1
    
    while(end_ptr.next):
        start_ptr = start_ptr.next
        end_ptr = end_ptr.next
    
    start_ptr.next = (start_ptr.next).next       
    return head
