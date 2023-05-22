from typing import List
from collections import defaultdict


# Topological sorting

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap = defaultdict(list)
        
        for a,b in prerequisites:
            premap[a].append(b)
        
        output = []
        cycle = set()
        visited = set()
        
        def dfs(a): 
            if a in cycle:
                return False
            if a in visited:
                return True
            cycle.add(a)
            
            for i in premap[a]:
                if not dfs(i):
                    return False
            cycle.remove(a) 
            visited.add(a) # we have traversed this course and dont need to traverse it again in future
            output.append(a)
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
       
        return output
        
        
print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))