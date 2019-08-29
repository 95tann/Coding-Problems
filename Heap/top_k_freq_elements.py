'''
Topic   : Heaps
Problem : Top K Frequent Elements
Link    : https://leetcode.com/problems/top-k-frequent-elements/
'''
import heapq as hq

def topKFrequent(nums,k):        
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    min_heap = []
    for key,val in freq.items():
        if len(min_heap) < k:
            hq.heappush(min_heap, (val,key))
        else:
            hq.heappushpop(min_heap, (val,key))
    
    k_freq_elements = []
    for item in min_heap:
        k_freq_elements.append(item[1])
    return k_freq_elements