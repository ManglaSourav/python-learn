from typing import List


# Complexity n^2  time and constant space

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # Storing top left value
                topleft = matrix[top][l+i]
                
                #bottom left to top left
                matrix[top][l+i] = matrix[bottom - i][l]
                
                # Bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # filling the temp to top right
                matrix[top+i][r] = topleft
                        
            l += 1
            r -= 1    
                
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix) #[[7,4,1],[8,5,2],[9,6,3]]


