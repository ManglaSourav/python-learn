from typing import List


class Solution:
    
    # tim complexity: O(N!)
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDia = set() # (r - c)
        posDia = set() # (r + c)
        
        board = [["."] * n for _ in range(n)]
        res = []
        
        def backtrack(r):
            # base case
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r-c) in negDia or (r+c) in posDia:
                    continue
                col.add(c)
                negDia.add(r-c) 
                posDia.add(r+c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col.remove(c)
                negDia.remove(r-c) 
                posDia.remove(r+c) 
                board[r][c] = "."
                
                      
            
        backtrack(0)
        return res
        

    
    
print(Solution().solveNQueens(4))