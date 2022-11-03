from typing import List

# in  2d array row is treated as count and cols have the list of values who has that number of count
# space and time complexity is O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for i in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res
        return res


k_freq = Solution()
print(k_freq.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 2))
