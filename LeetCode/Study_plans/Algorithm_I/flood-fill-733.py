
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        pixel = image[sr][sc]
        def dfs(r, c):
            if r < 0  or c < 0 or r >= ROWS or c >= COLS or image[r][c] != pixel or (r,c) in visited:
                return 
            
            visited.add((r,c))
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        
        dfs(sr, sc)
        return image


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))