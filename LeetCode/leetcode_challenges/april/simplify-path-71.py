# from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        values = path.split("/")
        for p in values:
            if p == "":
                continue
            elif p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)
    
print(Solution().simplifyPath("/a/./b/../../c"))

# /a/b/c
# "/c"