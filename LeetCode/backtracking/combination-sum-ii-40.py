from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(i, combs, c_sums):
            if target == c_sums:
                result.append(combs[:])
                return
            
            if target < c_sums or i == len(candidates):
                return 
            
            combs.append(candidates[i])
            backtrack(i+1, combs,candidates[i]+c_sums)

            combs.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1  
            backtrack(i+1, combs, c_sums)
    
        backtrack(0, [], 0)
        return result
    
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))