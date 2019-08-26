import check

''' 
Topic   : Recursion
Problem : Generate substrings
'''
def generate_substrings(string):
    substr_lst = []
    helper_substrings(string,"",substr_lst)
    return (substr_lst)

def helper_substrings(string,substring,lst):
    if string == "":
        lst.append(substring)
    else:
        helper_substrings(string[1:],substring+string[0],lst)
        helper_substrings(string[1:],substring,lst)

# Tests
print(check.expect(['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', ''],generate_substrings('abc')))
print(check.expect(['1234', '123', '124', '12', '134', '13', '14', '1', '234', '23', '24', '2', '34', '3', '4', ''],generate_substrings('1234')))



''' 
Topic   : Recursion
Problem : Generate subarray
''' 
def generate_subarray(arr):
    subarr_list = []
    helper_subarray(arr,[],subarr_list)
    return subarr_list

def helper_subarray(arr,subset,lst):
    if arr == []:
        lst.append(subset)
    else:
        helper_subarray(arr[1:],subset+[arr[0]],lst)
        helper_subarray(arr[1:],subset,lst)

# Tests
print(check.expect([['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []], generate_subarray(['a','b','c'])))
print(check.expect([[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2], [3, 4], [3], [4], []], generate_subarray([1,2,3,4])))
