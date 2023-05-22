


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            # print("calling dfs(i+1) for i = ", i)
            ans = dfs(i+1)
            if ((i < len(s)-1) and (int(s[i:i+2]) <= 26)):
                # print("calling dfs(i+2) for i = ", i)
  
                ans += dfs(i+2)
            dp[i] = ans
            return ans
        return dfs(0)
        
    
print(Solution().numDecodings("226"))