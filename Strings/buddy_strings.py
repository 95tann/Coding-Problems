'''
Topic   : Strings
Problem : Buddy Strings
Link    : https://leetcode.com/problems/buddy-strings/
'''

def buddyStrings(A, B):
    if A=='' or B=='': 
        return False
    
    elif A==B:
        if len(set(A)) >= len(A):
            return False
        else:
            return True
    
    elif len(A)==len(B) and set(A)==set(B):
        diff = []
        
        for char_A, char_B in zip(A,B):
            if char_A != char_B:
                diff.append((char_A,char_B))
        
        if diff==[]: 
            return True
        elif len(diff) == 2:
            return True if diff[0][0]==diff[1][1] and diff[0][1]==diff[1][0] else False
        else:
            return False
                
    elif len(A)==len(B) and set(A)!=set(B):
        return False
        
    else:
        return False