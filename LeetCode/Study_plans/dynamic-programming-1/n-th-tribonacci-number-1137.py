


class Solution:
    def tribonacci_simple(self, n: int) -> int:
        a = 0
        b = 1
        c = 1 
        if n < 2:
            return n
        
        for i in range(2,n):
            t1, t2 = c, b 
            c = a + b + c
            b = t1
            a = t2
        
        return c   
    # dfs         
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dfs(n1):
            if n1 in memo:
                return memo[n1]
            if n1 == 1 or n1 == 2:
                return 1
            if n1 == 0:
                return 0
            
            memo[n1] = dfs(n1-1) + dfs(n1-2) + dfs(n1-3)
            return memo[n1]
        
        return dfs(n)

print(Solution().tribonacci(4))