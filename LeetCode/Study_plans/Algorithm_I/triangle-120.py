from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            if i == len(triangle):
                return 0

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)

            return min(lower_left, lower_right)
            
        
        return dfs(0,0)
    
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))