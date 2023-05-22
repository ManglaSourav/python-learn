
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if len(edges) < 1 and n == 1:
            return True
        if len(edges) < 1 and n > 1:
            return False
        adj = defaultdict(list)
        
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        visited = set()
        print(adj)
        def dfs(node, prev):
            
            node_adj = adj[node]
            visited.add(node)
            for n in node_adj:
                if n != prev: # handling edge case
                   if n in visited:
                       return False
                   if not dfs(n, node):
                       return False 
            return True
        
        if not dfs(edges[0][0], -1):
            return False
        if len(visited) == n:
            return True
        else:
            return False    
    
    
print(Solution().valid_tree(8,[[0,1],[1,2],[3,2],[4,3],[4,5],[5,6],[6,7]]))