from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0
        for i in range(len(pushed)):
            
            while stack and popped[j] == stack[-1]:
                j+=1
                stack.pop()
            
            stack.append(pushed[i])
        
        while stack and popped[j] == stack[-1]:
                j+=1
                stack.pop()    
            
        if stack:
            return False
        return True
    
print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,1,2]))