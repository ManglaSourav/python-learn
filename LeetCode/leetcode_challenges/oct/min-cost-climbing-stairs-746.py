from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(costt, index):

        #     if index >= len(cost):
        #         return costt

        #     return min(dfs(costt+cost[index], index+1), dfs(costt+cost[index], index+2))

        # return min(dfs(0,0), dfs(0, 1))

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])

        return min(cost[0], cost[1])


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
