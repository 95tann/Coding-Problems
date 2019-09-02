'''
Topic   : Dynamic Programming
Problem : Longest Valid Parentheses
Link    : https://leetcode.com/problems/longest-valid-parentheses/
'''
def longestValidParentheses(s):
    if s == "": return 0

    str_len = len(s)
    DP = [0] * str_len

    for i in range(1,str_len):
        if s[i] == ")":
            if s[i-1] == "(":
                DP[i] = 2 if i<2 else DP[i-2]+2

            else:
                if (i-DP[i-1]-1)>=0 and s[i-DP[i-1]-1]=="(":
                    if i-DP[i-1]>=2:
                        DP[i] = 2 + DP[i-1] + DP[i-DP[i-1]-2]
                    else:
                        DP[i] = 2 + DP[i-1]

    return max(DP)