from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, i):
            # means found the word
            if i == len(word):
                return True
            # check left, right, up, down if not into visited
            
            if ((r < 0 )or 
                (c < 0 )or 
                (r > ROW-1) or 
                (c > COL-1) or ((r, c) in visited) or (board[r][c] != word[i])):
                return False
            
            visited.add((r, c))
            res =  dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            visited.remove((r, c))
            return res
            
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
                
        return False



print(Solution().exist(board = [["A","B","C","E"],
                                 ["S","F","C","S"],
                                 ["A","D","E","E"]]
, word = "SEE"))