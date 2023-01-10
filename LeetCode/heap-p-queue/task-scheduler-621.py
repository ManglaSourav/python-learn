from typing import List
import heapq
from collections import Counter, deque


class Solution:
    # O(m*n) time complexity
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()  # pairs of [-cnt, idleTime]
        time = 0
        count = Counter(tasks)
        intervals = [-x for x in count.values()]
        heapq.heapify(intervals)

        while intervals or q:
            time += 1

            if intervals:
                cnt = 1 + heapq.heappop(intervals)
                if cnt:
                    q.append([cnt, n + time])

            if q and q[0][1] == time:
                heapq.heappush(intervals, q.popleft()[0])

        return time


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], n=2))
