from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        result = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c): 
            # print(r,c)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for c in range(COLS):
            if (0, c) not in visited and grid[0][c] == 1:
                print(0, c)
                dfs(0, c)
            if (ROWS-1,c) not in visited and grid[ROWS-1][c] == 1:
                dfs(ROWS-1, c)

        
        for r in range(ROWS):
            if (r, 0) not in visited and grid[r][0] == 1:
                dfs(r, 0)
            if (r, COLS-1) not in visited and grid[r][COLS-1] == 1:
                dfs(r, COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    result += 1


        return result
    
    
    
print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))