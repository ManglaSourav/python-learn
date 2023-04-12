from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        visited = set()
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            
            if grid[r][c] == 1 or (r,c) in visited: # closed island
                return 1
            
            visited.add((r,c))
            
            return min(dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r,c-1))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0 and (r,c) not in visited:
                    if dfs(r, c):
                        result+=1
        
        return result 
    


print(Solution().closedIsland([[1,1,1,1,1,1,1,0],
                               [1,0,0,0,0,1,1,0],
                               [1,0,1,0,1,1,1,0],
                               [1,0,0,0,0,1,0,1],
                               [1,1,1,1,1,1,1,0]]))