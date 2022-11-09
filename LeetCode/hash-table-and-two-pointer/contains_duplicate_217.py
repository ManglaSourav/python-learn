from typing import List


# space complexity O(n) or  size of set or hashset
# time complexity O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for item in nums:
            if item in my_set:
                return True
            else:
                my_set.add(item)

        return False


duplicate = Solution()
print(duplicate.containsDuplicate([1, 2, 3, 1]))
