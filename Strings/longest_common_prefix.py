'''
Topic   : Strings
Problem : Longest Common Prefix
Link    : https://leetcode.com/problems/longest-common-prefix/
'''
def longestCommonPrefix(strs):
    if strs == []: return ""
    
    prefix = ""
    candidate = strs[0]
   
    for pos in range(0,len(candidate)):
        for string in range(1,len(strs)):
            if pos >= len(strs[string]): return prefix
            if strs[string][pos] != candidate[pos]: return prefix
        
        prefix += candidate[pos]
                    
    return prefix
