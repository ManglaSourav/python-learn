from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            # print("before 1st dfs", i, subset)
            dfs(i+1)

            # not include nums[i]
            subset.pop()
            # print("After 1st dfs", i, subset)
            dfs(i+1)
            # print("After 2nd dfs", i, subset)

        dfs(0)

        return res



print(Solution().subsets([1, 2, 3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
