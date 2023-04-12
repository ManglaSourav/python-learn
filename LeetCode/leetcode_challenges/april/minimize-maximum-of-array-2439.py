from typing import List
import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total/(i+1)))
            
        return res
    
    
print(Solution().minimizeArrayValue([3,7,1,6]))