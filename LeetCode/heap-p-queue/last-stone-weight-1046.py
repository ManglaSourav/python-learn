from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            res = abs(x-y)
            if res > 0:
                heapq.heappush(stones, -res)
        return -stones[0] if stones else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
