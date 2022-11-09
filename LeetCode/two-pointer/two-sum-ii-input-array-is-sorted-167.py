from typing import List


class Solution:
    def twoSum_sol1(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, n in enumerate(numbers):
            num = target - n
            if my_dict.get(num, -1) != -1:
                return [my_dict[num]+1, i+1]
            my_dict[n] = i
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left != right:

            if (numbers[left] + numbers[right] > target):
                right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1

            if(numbers[left] + numbers[right] == target):
                return [left+1, right+1]

        return []


two_sum = Solution()
print(two_sum.twoSum([2, 7, 11, 15], 9))
