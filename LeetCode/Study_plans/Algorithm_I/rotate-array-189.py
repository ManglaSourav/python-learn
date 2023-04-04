
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
        
    def reverse(self, nums, left, right):
        print(left, " - ", right)
        
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)
# 5,6,7,1,2,3,4