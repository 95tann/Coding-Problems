''' 
Problem : Pascal's Triangle
Link    : https://leetcode.com/problems/pascals-triangle/
'''

def generate_triangle(numRows):
        if numRows == 0:
            return []
       
        elif numRows == 1:
            return [[1]]
       
        elif numRows == 2:
            return [[1],[1,1]]
        
        else:
            result =  [[1],[1,1]]
            for curr_row in range(3,numRows+1):
                new_row = [1]*curr_row
        
                for i in range(1,curr_row-1):
                    new_row[i] = result[curr_row-2][i-1] + result[curr_row-2][i]
                
                result.append(new_row)
            
            return result
            