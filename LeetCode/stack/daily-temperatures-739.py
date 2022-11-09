from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair of value and index
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                output[index] = i - index
            stack.append((i, t))

        return output


temp = Solution()
print(temp.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1,1,4,2,1,1,0,0]
