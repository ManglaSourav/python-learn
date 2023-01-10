from typing import List
import heapq


class Solution:
    def findKthLargest_simple(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)

    def findKthLargest_sorting(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        
        def quick_select(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums)-1)


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
