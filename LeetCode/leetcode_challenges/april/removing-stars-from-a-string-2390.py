from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack  = deque()
        
        for c in s:
            
            if c == "*":
                stack.pop()
                
            else:
                stack.append(c)
        res = ""
        print(stack)
        while stack:
            res += stack.popleft()
        return res
    
print(Solution().removeStars("leet**cod*e"))