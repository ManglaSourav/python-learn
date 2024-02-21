from collections import deque


class Solution:
    def getWinner(self, arr, k: int) -> int:

        q = deque(arr[1:])
        curr = arr[0]
        streak = 0

        while q:
            val = q.popleft()
            if curr > val:
                streak += 1
                q.append(val)
            else:
                streak = 1
                q.append(curr)
                curr = val

            if streak == k:
                return curr


print(Solution().getWinner([2, 1, 3, 5, 4, 6, 7], 2))
