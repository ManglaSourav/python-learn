


# O(n) time and space complexity

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * n
        
        def dfs(temp):
            if temp == n:
                return 1
            elif temp > n:
                return 0
            elif dp[temp] != -1:
                return dp[temp]
            else:
              dp[temp] = dfs(temp + 1) + dfs(temp + 2)
              return dp[temp] 
          
        return dfs(0)
    

    
print(Solution().climbStairs2([1,100,1,1,1,100,1,1,100,1]))
