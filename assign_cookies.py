'''
Topic   : Arrays
Problem : Assign Cookies
Link    : https://leetcode.com/problems/assign-cookies/
'''
def findContentChildren(g, s):
    i, j, count = 0, 0, 0
    sorted_cookies, sorted_greed = sorted(s), sorted(g)
    
    while(i<len(s) and j<len(g)):
        if sorted_cookies[i] >= sorted_greed[j]:
            count += 1
            i += 1
            j += 1
        else:
            i+=1
         
    return count
