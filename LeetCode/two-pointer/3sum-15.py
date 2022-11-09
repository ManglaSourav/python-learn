from typing import List

# Complexity: Sorting O(nlogn) + O(n^2) for two pointer for n values = total O(n^2)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:  # if number is already used
                continue
            left = i+1
            right = len(nums) - 1
            target = -n
            while left < right:
                if (nums[left]+nums[right] > target):
                    right -= 1
                elif (nums[left]+nums[right] < target):
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    # we need to update left pointer other it will pick the same triplet again and again in infintite loop
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result


three_sum = Solution()
print(three_sum.threeSum([-1, 0, 1, 2, -1, -4]))
