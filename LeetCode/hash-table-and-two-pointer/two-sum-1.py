from typing import List
from collections import defaultdict

# O(n) is the time and space complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            if my_dict.get(diff, -1) != -1: # if i found the difference in map return the index.
                return [my_dict[diff], i]
           
            my_dict[nums[i]] = i
        
        return []


two_sum = Solution()
print(two_sum.twoSum([3, 3], 6))
