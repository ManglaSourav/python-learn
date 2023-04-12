from typing import List
from collections import defaultdict
class Solution:
    
    # complexity 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # making adjacency list
        premap = defaultdict(list)
        for a, b in prerequisites:
            premap[a].append(b)
        
        
        
        visited = set()
        
        def dfs(a):
            
            if a in visited:
                return False
            elif premap[a] == []:
                return True
            visited.add(a)
            
            for b in premap[a]:
                if not dfs(b):
                    return False
            visited.remove(a)
            premap[a] = []
            return True
            
            
        
        for a, b in prerequisites:
            if not dfs(a):
                return False
        
        return True

        
    
    
print(Solution().canFinish(2, prerequisites = [[1,0]]))