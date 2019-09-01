'''
Topic   : Dynamic Programming
Problem : Longest Valid Parentheses
Link    : https://leetcode.com/problems/longest-valid-parentheses/
'''
def longest_valid_parentheses(input_string):
    if input_string == "": return 0
    
    str_len = len(input_string)
    to_balance_len, longest_len = 0, 0
    DP = [0] * str_len

    for i in range(str_len):
        if input_string[i] == ")" and to_balance_len > 0:
            j = i-DP[i-1]-1
            to_balance_len -= 1
            
            if input_string[j] == '(':
                DP[i] = 2 + DP[i-1]
                if j-1 >= 0: 
                    DP[i] += DP[j-1]
                longest_len = max(DP[i], longest_len)
        
        if input_string[i] == "(":
            to_balance_len += 1
    
    return longest_len