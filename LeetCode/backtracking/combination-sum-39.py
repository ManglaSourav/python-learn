from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        res = []
        
        def dfs(i , curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i]) # not i+1 because we can reuse same elements
            
            curr.pop()
            dfs(i+1, curr, total) # i+1 because we can't reuse same elements for the right subtree
        
        dfs(0, [], 0)
        return res
    
print(Solution().combinationSum([2,3,6,7], 7))