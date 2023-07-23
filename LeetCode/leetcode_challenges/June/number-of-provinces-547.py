from typing import List
from collections import defaultdict, deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        n = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i].append(j)
        visited = set()
        res = 0
        
        def bfs(i):
            nonlocal res
            q = deque([i])
            visited.add(i)
            while q:
               node = q.popleft()
               for nei in adj[node]:
                   if nei not in visited:
                       visited.add(nei)
                       q.append(nei)
            
            res += 1            
            
        for i in range(n):
            if i not in visited:
                bfs(i)
            
        return res   



def findRedundantConnection(edges):
    parent = [i for i in range(len(edges) + 1)] # not going to use 0th index
    rank = [1] * (len(edges) + 1)
    print(parent, rank)
    
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
        union(n1, n2)
    #     if not union(n1, n2):
    #         return [n1, n2]
        

data = [[1,0,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,1,1]]


print(Solution().findCircleNum(data))
# print(findRedundantConnection(data))
    
    