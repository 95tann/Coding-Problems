'''
Topic   : Arrays
Problem : Merge Two Sorted Arrays
Link    : https://leetcode.com/problems/merge-sorted-array/
'''
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m,len(nums1)):
        nums1[i] = 'x'
   
    ptr1, ptr2 = 0,0
    while(ptr2 < n and (ptr1<m or nums1[ptr1]!='x')):
        if nums1[ptr1] <= nums2[ptr2]:
            ptr1 += 1
        else:
            nums1.insert(ptr1,nums2[ptr2])
            nums1.pop()
            ptr1 += 1
            ptr2 += 1
    
    while(ptr2 < n):
        nums1[ptr1] = nums2[ptr2]
        ptr1 += 1
        ptr2 += 1
    
    return