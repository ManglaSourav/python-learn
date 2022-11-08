from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []

        def backtrack(openN, closedN):
            print(stack)
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                # print("before open - ", openN, "-", closedN)
                backtrack(openN+1, closedN)
                # print("After open - ", openN, "-", closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                # print("before closed - ", openN, "-", closedN)
                backtrack(openN, closedN+1)
                # print("After closed - ", openN, "-", closedN)
                stack.pop()
                
        backtrack(0, 0)
        return result


paren = Solution()
print(paren.generateParenthesis(3))
