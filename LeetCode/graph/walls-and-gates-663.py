from typing import (
    List,
)
from collections import deque


# complexity: O(m*n)
class Solution:
    
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))
        
        while q:
            
            l = len(q)

            for i in range(l):
                
                r, c = q.popleft()
                
                for row, col in [(1,0),(0,1),(-1,0), (0,-1)]:
                    n_r = r+row
                    n_c = c+col
                    if 0 <= n_r < ROWS and 0<= n_c <COLS and (n_r,n_c) not in visited and rooms[n_r][n_c]==2147483647:
                        visited.add((n_r, n_c))
                        rooms[n_r][n_c] = 1 + rooms[r][c]
                        q.append((n_r, n_c))
        
        return rooms 
print(Solution().walls_and_gates([[2147483647,-1,0,2147483647],
                                  [2147483647,2147483647,2147483647,-1],
                                  [2147483647,-1,2147483647,-1],
                                  [0,-1,2147483647,2147483647]]))
