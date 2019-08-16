'''
Topic   : Strings
Problem : Excel Sheet Column Number
Link    : https://leetcode.com/problems/excel-sheet-column-number/
'''
def titleToNumber(s):
    col_num = 0
    len_s = len(s)
   
    for i in range(1,len_s+1):
        char = s[len_s - i].lower()
        col_num += (ord(char)-96) * (26 ** (i-1))
    
    return col_num