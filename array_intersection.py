''' 
Topic   : Arrays
Problem : Intersection of Two Arrays
Link    : https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
def intersect(nums1, nums2):
    intersect = []
    
    for num in nums1:
        if num in nums2:
            nums2.remove(num)
            intersect.append(num)
    
    return intersect