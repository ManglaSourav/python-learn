from typing import List
from collections import deque


class Solution:
    # inefficient
    def maxSlidingWindow_sol1(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        result = []
        while r < len(nums):
            arr = sorted(nums[l:r+1])
            result.append(arr[k-1])
            r += 1
            l += 1

        return result

    # O(n) complexity

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = deque()
        result = []

        while r < len(nums):
            # pop from right till queue is empty or find the larger value for the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:  # left index is out of bound
                q.popleft()

            if (r-l+1) == k:
                result.append(nums[q[0]])
                l += 1

            r += 1

        return result


max_slide = Solution()
print(max_slide.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
