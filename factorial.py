'''
Topic   : Recursion
Problem : Finding Factorials
'''
import check

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Tests
print(check.expect(1,(factorial(0))))
print(check.expect(1,factorial(1)))
print(check.expect(40_320,factorial(8)))
print(check.expect(2_432_902_008_176_640_000,factorial(20)))