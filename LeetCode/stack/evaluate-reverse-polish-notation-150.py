from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token in ["+", "*", "/", "-"]:

                num1 = stack.pop()
                num2 = stack.pop()
                val = 0
                if token == "+":
                    val = num1 + num2
                elif token == "-":
                    val = num2 - num1
                elif token == "*":
                    val = num1 * num2
                elif token == "/":
                    val = int(num2 / num1)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[0]


rpm = Solution()
print(rpm.evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
