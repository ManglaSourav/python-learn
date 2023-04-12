


from typing import List



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res= []
        
        def backtract(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
        
            for i in range(start, n+1):
                comb.append(i)
                backtract(i+1, comb)
                comb.pop()

        backtract(1, [])
        return res
        
    
print(Solution().combine(4, 2))