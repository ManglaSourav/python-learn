from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
                
        
        row_counter = Counter(tuple(row) for row in grid)
        
        count = 0
        print(row_counter)
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count
        
    
print(Solution().equalPairs([[3,2,3],
                             [1,7,2],
                             [3,2,3]]))