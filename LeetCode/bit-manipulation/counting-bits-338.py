from typing import List

class Solution:
    
    def countBits_simple(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        
        return res
    
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            
            if offset *2 == i:
                offset = i
            dp[i] = dp[i-offset] + 1
            
        return dp
    
print(Solution().countBits(5))


