from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        q = []
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = "#"
        
        
        direction = [(1,0), (-1,0), (0,1),(0,-1)]
        
        for row, col in q:
            for r,c in direction:
                new_r = row+r
                new_c = col+c
                if 0 <= new_c < COLS and 0 <= new_r < ROWS and mat[new_r][new_c]=="#":
                    mat[new_r][new_c] = 1+ mat[row][col]
                    q.append((new_r, new_c))
        
        
        return mat


print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
        
        
                    
        