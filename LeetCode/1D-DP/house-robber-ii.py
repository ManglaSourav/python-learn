
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def get_sum(n):
            rob1, rob2 = 0, 0
            
            for i in n:
                temp = max(rob1+i, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
    
        return max(nums[0], get_sum(nums[:len(nums) - 1]), get_sum(nums[1:]))
    
    
print(Solution().rob([1]))