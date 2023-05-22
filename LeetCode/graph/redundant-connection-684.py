from typing import List

# Disjoint set or union find method
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # not going to use 0th index
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # speeding up the operation of finding parent
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: # means both node has the same edge which is redundant
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        
print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))