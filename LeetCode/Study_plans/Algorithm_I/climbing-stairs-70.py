
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
#    1 1 2 3 5 8 13
print(Solution().climbStairs(6))