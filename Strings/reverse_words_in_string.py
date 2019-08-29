'''
Topic   : Strings
Problem : Reverse Words in a String III
Link    : https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''
def reverse_str(s):
    reversed_str = ''
    for i in reversed(range(len(s))):
        reversed_str += s[i]
    return reversed_str

def reverseWords(s):
    word_list = s.split(" ")
    reverse_words = map(reverse_str,word_list)
    return ' '.join(reverse_words)