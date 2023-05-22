
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
    
'''
n = 5
0 0 0 0 0
1 1 1 1 1
1 0 1 0 1
1 0 0 0 1
1 0 0 0 0 
'''
print(Solution().bulbSwitch(5))