from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        
        top, bottom = 0, n
        left, right = 0, n
        num = 1
        while left < right and top < bottom:
            
            for i in range(left, right):
                res[top][i] = num
                num+=1
            top+=1
            
            for i in range(top, bottom):
                res[i][right-1] = num
                num+=1
            right-=1
            
            if left >= right or top >= bottom:
                break
            
            for i in range(right-1, left-1, -1):
                res[bottom-1][i] = num
                num+=1
            bottom-=1
            
            for i in range(bottom-1, top-1,-1):
                res[i][left]=num
                num+=1
            left+=1
    
    
        return res
    
    
print(Solution().generateMatrix(3))