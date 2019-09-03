'''
Topic   : Dictionaries
Problem : Contains Duplicate II
Link    : https://leetcode.com/problems/contains-duplicate-ii/
'''
def containsNearbyDuplicate(nums, k):
    num_dict = {}
    
    for i, num in enumerate(nums):
        if num not in num_dict:
            num_dict[num]=i
        else:
            if i-num_dict[num] <= k:
                return True
            else:
                num_dict[num]=i
            
    return False