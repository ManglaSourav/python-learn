
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
       
        
        memo = {}
        def dfs(i):
            
            if i >= len(questions):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(questions[i][0]+dfs(i+1+questions[i][1]), dfs(i+1))
            
            return memo[i]
        
        
        return dfs(0)
    
print(Solution().mostPoints([[12,46],[78,19],[63,15],[79,62],[13,10]]))