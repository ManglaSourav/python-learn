from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"}":"{","]":"[",")":"("} 
        stack = deque()
        for i in s:
            if i in my_dict:
                if stack and stack[-1] == my_dict.get(i,""):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        print(stack) 
        if stack:
            return False
        return True
    
    
print(Solution().isValid("["))