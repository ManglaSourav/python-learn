from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: 
        
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                    

        while q:
            
            l = len(q)
            for i in range(l):
                result += 1
                
                
                
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
                
        return result = 0
                
    
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))