
class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = { ")": "(", "}":"{","]":"[" }
        stack  = []
        
        for i in s:
           print(stack)
           if i in my_dict:
            # pop till dict matched
                if stack and stack[-1] == my_dict.get(i,""):
                    stack.pop()
                else:
                    return False
           else:
               stack.append(i) 

        if stack:
            return False
        return True
    

print(Solution().isValid("()[{}]"))