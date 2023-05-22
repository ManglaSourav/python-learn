from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0]* len(graph) 
        
        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[i] == odd[nei]: # if neighor and current node has same color or val then return false
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i]

            return True
            
            
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
    
print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))