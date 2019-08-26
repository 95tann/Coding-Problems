''' 
Topic   : Dynamic Programming
Problem : Candy Count
Link    : https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
'''
def candies(n, arr):
    forward = [1] * n
    backward = [1] * n
    
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            forward[i] = 1 + forward[i-1]

    for j in range(1,n):
        if arr[n-j-1] > arr[n-j]:
            backward[j] = 1 + backward[j-1] 
    
    candie_count = 0
    x,y = 0, n-1
    while x < n:
        candie_count += max(forward[x],backward[y])
        x += 1
        y -= 1
    
    return candie_count
