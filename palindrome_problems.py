import check

'''
Topic   : Palindromes
Problem : https://leetcode.com/problems/valid-palindrome/
'''
def is_palindrome(string):
    if len(string) in [0,1]:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return True and is_palindrome(string[1:-1])

# Tests
print(check.expect(True, is_palindrome("")))
print(check.expect(True,is_palindrome("hahah")))
print(check.expect(True, is_palindrome("123454321")))
print(check.expect(True,is_palindrome("loooooooooooooooooooooooool")))
print(check.expect(False,is_palindrome("joker")))
print(check.expect(False,is_palindrome("1224")))


'''
Topic   : Palindromes
Problem : https://leetcode.com/problems/longest-palindromic-substring/
'''
def palindrome_helper(string,left,right):
    if left == right:
        return 1
    else:
        if left+1 == right:
            if string[left] == string[right]:
                return 2
            else:
                return max(palindrome_helper(string,left,right-1),palindrome_helper(string,left+1,right))
        else:
            if string[left] == string[right]:
                return (2 + palindrome_helper(string,left+1,right-1))
            else:
                return max(palindrome_helper(string,left,right-1),palindrome_helper(string,left+1,right))


def find_longest_palindrome_subsequence(string):
    if len(string) in [0,1]:
        return len(string)

    return palindrome_helper(string,0,len(string)-1)

# Tests
print(check.expect(9,find_longest_palindrome_subsequence('abaxabaxabb')))
print(check.expect(2,find_longest_palindrome_subsequence('hello')))
print(check.expect(4,find_longest_palindrome_subsequence('noon')))
print(check.expect(7,find_longest_palindrome_subsequence('abaaaaabi')))
print(check.expect(0,find_longest_palindrome_subsequence('')))
print(check.expect(5,find_longest_palindrome_subsequence('caaacoo')))
print(check.expect(1, find_longest_palindrome_subsequence('Z')))