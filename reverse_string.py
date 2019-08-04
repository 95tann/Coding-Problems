'''
Problem : Reverse String 
Topic   : Recursion
'''
import check

def reverse_str(string):
    if string == "":
        return ""
    else:
        return string[-1] + reverse_str(string[:-1])

# Tests
print(check.expect("", reverse_str("")))
print(check.expect("aba", reverse_str("aba")))
print(check.expect("54321", reverse_str("12345")))