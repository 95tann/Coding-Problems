'''
Topic   : Arrays
Problem : K Different Pairs
Link    : https://leetcode.com/problems/k-diff-pairs-in-an-array/
'''
def findPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k < 0: return 0
    
    nums.sort()
    pair_set = set()
    i, j = 0, 1
    pair_count = 0
  
    while(j < len(nums)):            
        if nums[j]-nums[i]==k:
            if (nums[i],nums[j]) not in pair_set:
                pair_count += 1
                pair_set.add((nums[i],nums[j]))
            i += 1
            j += 1
        elif nums[j]-nums[i] < k:
            j += 1
        else:
            i += 1
    
        if i==j: j += 1
            
    return pair_count