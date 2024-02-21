from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}

        def dfs(i, remain):

            if (i, remain) in dp:
                return dp[(i, remain)]
            if remain <= 0:
                return 0
            if i >= len(cost):
                return float("inf")

            paint = cost[i] + dfs(i+1, remain - 1 - time[i])
            skip = dfs(i+1, remain)
            dp[(i, remain)] = min(paint, skip)

            return dp[(i, remain)]

        return dfs(0, len(cost))


print(Solution().paintWalls(cost = [2,3,4,2], time = [1,1,1,1]))
