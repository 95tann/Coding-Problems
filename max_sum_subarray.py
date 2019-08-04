import check

'''
Topic  : Dynamic Programming
Problem: Given an array of int, arr, find the contiguous subset of elements, 
         such that the sum of elements in the contiguous subset is maximed
'''
def max_sum_subarray(arr): #KADANE's algorithm
    if arr == []:
        return([],0)

    local_max, local_start, local_end = arr[0], 0, 1    
    global_max, global_start, global_end = arr[0], 0, 1

    for i in range(1,len(arr)):
        if (arr[i]+local_max) > arr[i]:
            local_max = arr[i]+local_max
            local_end = i+1

        else:
            local_max = arr[i]
            local_start, local_end = i, i+1


        if local_max > global_max:
            global_max = local_max
            global_start = local_start
            global_end = local_end

    return (arr[global_start:global_end],global_max)

# Tests
print(check.expect(([], 0),max_sum_subarray([])))
print(check.expect(([2], 2),max_sum_subarray([2])))
print(check.expect(([-1], -1),max_sum_subarray([-1])))
print(check.expect(([1, 0, 3, 5], 9), max_sum_subarray([-2,1,0,3,5])))
print(check.expect(([1, 2, 3, 4, 5], 15),max_sum_subarray([1,2,3,4,5])))
print(check.expect(([0], 0),max_sum_subarray([-1,-2,-3,0,-4])))
print(check.expect(([-1], -1), max_sum_subarray([-5,-2,-3,-10,-1])))
print(check.expect(([5], 5),max_sum_subarray([-2,1,3,-4,5])))
print(check.expect(([3, 2], 5),max_sum_subarray([-2,3,2,-1])))
print(check.expect(([2, 1], 3),max_sum_subarray([1,-3,2,1,-1])))
