from typing import List

# O(n) with no extra space.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * postfix
            postfix *= nums[i]

        return output


prod = Solution()
print(prod.productExceptSelf([1, 2, 3, 4]))
