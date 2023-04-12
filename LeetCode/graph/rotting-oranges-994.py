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
            result += 1
            for i in range(l):
                r, c = q.popleft()
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_r = r+i
                    new_c = c+j
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c]==1:
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))         
        if result > 0:
            result -= 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
                
        return result
                
    
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))