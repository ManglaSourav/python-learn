
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        res = []
        for i in candies:
            if i+extraCandies >= max_val:
                res.append(True)
            else:
                res.append(False)
        return res
                 
    
print(Solution().kidsWithCandies([2,3,5,1,3], extraCandies = 3))