
from typing import List


# O(m*n) time and constant space

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        
        while left < right and top < bottom:
            
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right, left, -1):
                res.append(matrix[bottom-1][i-1])
            bottom -= 1
            
            for i in range(bottom, top, -1):
                res.append(matrix[i-1][left])
            left += 1    
            
        return res
    
# print(Solution().spiralOrder([[1,2,3]]))
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]