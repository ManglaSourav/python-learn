from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n1 = cost[0]
        # n2 = cost[1]
        
        # for i in range(2, len(cost)):
        #     n1 = 
        pass
        
    
    
    def minCostClimbingStairs_easy(self, cost: List[int]) -> int:
        
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
    
    

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))