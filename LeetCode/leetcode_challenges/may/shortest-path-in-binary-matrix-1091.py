from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        res = -1
        ROW, COL = len(grid)-1, len(grid)-1
        visited = set()
        def dfs(i, j, count):
            nonlocal res
            if i > ROW or j > COL or i < 0 or j < 0 or grid[i][j] == 1 or (i,j) in visited:
                return
            
            visited.add((i, j))
            print(i, j, count)
            if i == ROW and j == COL:
                if res == -1:
                    res = count
                else:
                    res = min(res, count+1)
                print("res", res)
                return
            
            directions = [
                [i-1, j],
                [i+1, j],
                [i, j-1],
                [i, j+1],
                [i-1, j-1],
                [i+1, j+1],
                [i-1, j+1],          
                [i+1, j-1]]
            
            for a, b in directions:
                if (a, b) not in visited:
                    dfs(a, b, count+1)
        
        dfs(0, 0, 0)
        
        return res
    
    
print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))