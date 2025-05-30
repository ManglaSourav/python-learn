

class Solution:
    # recursive or top down
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        
        def dfs(i, j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j) 
            else: 
                cache[(i, j)] = dfs(i+1, j) 
            
            return cache[(i, j)]
            
        return dfs(0,0)
    
    def numDistinct_bottom_up(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        
        for j in range(len(t)):
            cache[(len(s), j)] = 0
            
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]
    
    
    
print(Solution().numDistinct(s = "abcbabc", t = "abc"))