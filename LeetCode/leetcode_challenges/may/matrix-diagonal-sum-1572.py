from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROW, COL = len(mat), len(mat)
        sum = 0
        dec = True
        t = 0
        b = ROW-1
        for c in range(COL):
            if t == b == c:
                sum += mat[t][c]
                dec = False
            else: 
                sum += mat[t][c] + mat[b][c]
            
            if dec:
                t+=1
                b-=1
            else:
                t-=1
                b+=1
                
        return sum
    

print(Solution().diagonalSum([[1,2,3],
                              [4,5,6],
                              [7,8,9]]))