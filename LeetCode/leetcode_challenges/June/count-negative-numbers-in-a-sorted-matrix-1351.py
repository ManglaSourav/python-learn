from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        res = 0
        n = len(grid[0])

        for row in grid:
            
            right = len(row) - 1
            left = 0
            
            while right >= left:
                # print(row)
                mid = (right+left)//2
                
                if row[mid] < 0:
                    right = mid - 1
                    break
                else:
                    left = mid + 1
            res += (n - left)
        return res            
            
print(Solution().countNegatives([[4,3,2,-1],
                                 [3,2,1,-1],
                                 [1,1,-1,-2],
                                 [-1,-1,-2,-3]]))