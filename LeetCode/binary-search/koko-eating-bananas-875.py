from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        result = right
        
        while left <= right:
            k = (left+right)//2
            # print(k, "-", left, "-", right)
            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(pile/k)

            if temp_h <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1

        return result


eating = Solution()
print(eating.minEatingSpeed([3, 6, 7, 11], 8))
