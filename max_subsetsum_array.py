import check

'''
Topic  : Dynamic Programming
Problem: Given an array of int, arr, find the subset of elements, s, 
         such that the sum of elements in s is maximed
'''
def max_subsetsum_array(arr):
    """ Given an array of int, arr, find the subset of elements, s, 
    such that the sum of elements in s is maximed """

    if arr == []:
        return ([],0)

    max_sum = arr[0]
    max_subsetsum_array = arr[0:1]

    for i in range(1,len(arr)):
        if((arr[i]+max_sum)>max_sum and (arr[i]+max_sum)>arr[i]):
            max_sum = arr[i] + max_sum
            max_subsetsum_array.append(arr[i])
        
        if(arr[i]>max_sum and arr[i]>(max_sum + arr[i])):
            max_sum = arr[i]
            max_subsetsum_array = [arr[i]]

    return(max_subsetsum_array,max_sum)

# Tests
print(check.expect(([],0), max_subsetsum_array([])))
print(check.expect(([2], 2), max_subsetsum_array([2])))
print(check.expect(([-1], -1), max_subsetsum_array([-1])))
print(check.expect(([1, 3, 5], 9), max_subsetsum_array([-2,1,0,3,5])))
print(check.expect(([1, 2, 3, 4, 5], 15), max_subsetsum_array([1,2,3,4,5])))
print(check.expect(([0], 0), max_subsetsum_array([-1,-2,-3,0,-4])))
print(check.expect(([-1], -1), max_subsetsum_array([-5,-2,-3,-10,-1])))
print(check.expect(([1, 3, 5], 9), max_subsetsum_array([-2,1,3,-4,5])))