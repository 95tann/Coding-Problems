'''
Topic   : Arrays
Problem : Third Max Number
Link    : https://leetcode.com/problems/third-maximum-number/
'''

def thirdMax(nums):
    top3 = []
    
    for num in set(nums):
        if len(top3) < 3:
            top3.append(num)
            top3.sort(reverse=1)
        else:
            if top3[-1] < num:
                top3.pop()
                top3.append(num)
                top3.sort(reverse=1)
        
    return top3[-1] if len(top3)==3 else top3[0]