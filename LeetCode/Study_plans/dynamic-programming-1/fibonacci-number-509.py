

memo = {}
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if not memo.get(n-1, 0):
             memo[n-1] = self.fib(n-1)
        if not memo.get(n-2, 0):
            memo[n-2] = self.fib(n-2)   
        return memo[n-1] + memo[n-2]
        
    
print(Solution().fib(5))