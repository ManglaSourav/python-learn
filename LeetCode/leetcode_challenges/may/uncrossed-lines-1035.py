from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # res = 0
        memo = {}
        
        def findUncrossedLine(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            if memo.get((i, j), 0):
                return memo[(i, j)]
            
            if nums1[i] == nums2[j]:
                memo[(i, j)] = findUncrossedLine(i+1, j+1) + 1
                return memo[(i, j)]
            
            
            memo[(i, j)] = max(findUncrossedLine(i, j+1), findUncrossedLine(i+1,j))
            return memo[(i, j)]
            
        
        return findUncrossedLine(0, 0)
        
        
    
    
print(Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))