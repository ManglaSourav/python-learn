import heapq

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            n1 = -heapq.heappop(stones)
            n2 = -heapq.heappop(stones)
            print(n1, n2)
            heapq.heappush(stones, -(n1-n2))
            
        return -heapq.heappop(stones)
    
print(Solution().lastStoneWeight([2,7,4,1,8,1]))