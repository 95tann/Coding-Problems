'''
Topic   : Dictionaries
Problem : First Unique Character
Link    : https://leetcode.com/problems/first-unique-character-in-a-string/
'''
def firstUniqChar(s):
    char_dict = {}
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    min_index = -1
    for i, char in enumerate(s):
        if char_dict[char] == 1:
            return i
    return min_index