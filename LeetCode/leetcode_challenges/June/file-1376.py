
from collections import defaultdict, deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            graph[m].append(i)
        
        
        # print(graph)
        
        q = deque([(headID, informTime[headID])])
        res = 0
        while q:
            
            i, time = q.popleft()
            res = max(res, time)
            for nei in graph[i]:
                q.append((nei, time + informTime[nei]))
        
        return res
        
        # def dfs(i):
            
        #     maxTime = max( [ dfs(j) for j in graph[i]]  or [0])
        #     return  maxTime + informTime[i]
        
        # return dfs(headID)
    

print(Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))