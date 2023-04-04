from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        col = len(grid[0])
        visited = set()
        
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= col or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, dfs(r,c))
        
        return area
    
    
    def maxAreaOfIsland_bfd(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        col = len(grid[0])
        visited = set()
        
        def bfs(r, c):
            visited = set()
            q = deque()
            dir = [(0,1), (0,-1), (1,0), (-1,0)]
            q.append((r,c))
            visited.add((r,c))
            count = 0
            while q:
                r, c = q.popleft()
                count += 1
                for d in dir:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < rows and 0 <= nc < col and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return count
        
        
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, bfs(r,c))
        
        return area
    
    
print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,1,0,0,0,0],
                                  [0,0,1,0,0,0,0,1,1,0,0,0,0]
                                  ]))