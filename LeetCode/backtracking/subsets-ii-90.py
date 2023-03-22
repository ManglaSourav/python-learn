from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        
        
        def dfs(i):
            if i == len(nums):
                result.append(subset[:])
                return
            
            # add left side and do not add right side
            subset.append(nums[i])
            print("left ",subset, " i=", i)
            dfs(i+1)
            
            subset.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
            
        
        dfs(0)
        return result
            
        
        

print(Solution().subsetsWithDup([1,2,2]))