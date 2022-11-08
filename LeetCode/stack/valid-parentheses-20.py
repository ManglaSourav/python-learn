from collections import deque


class Solution:

    def isValid(self, s: str) -> bool:
        stack = deque()
        my_dict = {")": "(", "}": "{", "]": "["}

        for c in s:
            curr = my_dict.get(c, "")
            if c in my_dict:  # if closing bracket is coming
                if stack and stack[-1] == curr:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        return True


valid_param = Solution()
print(valid_param.isValid("()"))

# ()[]{}
