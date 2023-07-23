

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1
        
        
        directions = [[-2,-1], [-2, 1], [-1, -2], [-1, 2],
                          [2,-1],  [2,1],  [1, -2],  [1, 2]]
        
        for moves in range(1, k+1):
            
            for i in range(n):
                for j in range(n):
                    # Iterate over possible directions
                    for direction in directions:
                        prev_i, prev_j = i - direction[0], j - direction[1]
                        # Check if the previous cell is within the chessboard
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            # Add the previous probability
                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]
                    # Divide by 8
                    dp[moves][i][j] /= 8
        
        return sum(
            dp[k][i][j]
            for i in range(n)
            for j in range(n)
        )
    
print(Solution().knightProbability(n = 3, k = 2, row = 0, column = 0))