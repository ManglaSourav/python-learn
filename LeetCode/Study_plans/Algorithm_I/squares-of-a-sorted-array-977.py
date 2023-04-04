
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) -1
        # adjusting the values first according to the highest abs values
        new_nums = [0]*len(nums)
        i = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                new_nums[i] = abs(nums[left])
                left += 1
            else:
                new_nums[i] = abs(nums[right])
                right -= 1
            i -= 1
            
        return [x**2 for x in new_nums]
    

print(Solution().sortedSquares([-7,-3,2,3,11]))