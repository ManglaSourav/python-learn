from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water


trap = Solution()
print(trap.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
