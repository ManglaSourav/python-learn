from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        sett = set()
        for f,t in edges:
            sett.add(t)
        res = []
        for i in range(n):
            if i not in sett:
                res.append(i)
        
        return res
    
    
print(Solution().findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))