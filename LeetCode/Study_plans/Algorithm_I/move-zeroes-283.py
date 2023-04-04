from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        left, right = 0, 1
        while right < len(nums) and left < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                
            while left < len(nums) and nums[left] != 0:
                left += 1
                if left > right:
                    right+=1
                
            while right < len(nums) and  nums[right] == 0:
                right += 1

nums = [4,2,4,0,0,3,0,5,1,0]
Solution().moveZeroes(nums)
print(nums)