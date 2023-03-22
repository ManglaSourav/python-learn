

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
       
        return str(bin(start ^ goal)[2:]).count('1')
          
    
print(Solution().minBitFlips(10, 7))