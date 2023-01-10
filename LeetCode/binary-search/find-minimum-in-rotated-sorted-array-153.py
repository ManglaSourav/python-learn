from typing import List
import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        min_value = nums[0]
        while left <= right:

            if nums[left] < nums[right]:
                min_value = min(min_value, nums[left])
                break

            mid = (left+right)//2
            min_value = min(min_value, nums[mid])

            # left sorted array
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return min_value


find = Solution()
print(find.findMin([3, 4, 5, 1, 2]))
