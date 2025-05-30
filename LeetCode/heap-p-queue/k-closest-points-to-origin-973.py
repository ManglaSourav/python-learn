from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        # print(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], k=2))
