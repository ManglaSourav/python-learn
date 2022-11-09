from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        long_sequence = 0
        for n in nums:
            if n-1 not in my_set:             # check left of n in set

                seq_length = 0
                while n + seq_length in my_set:
                    seq_length += 1
                long_sequence = max(long_sequence, seq_length)

        return long_sequence


long_cons = Solution()
print(long_cons.longestConsecutive([100, 4, 200, 1, 3, 2]))
