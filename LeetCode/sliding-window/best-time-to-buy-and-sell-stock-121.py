from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_price = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_price = max(max_price, profit)
            else:
                left = right  # we found the new lowest
            right += 1
        return max_price


profit = Solution()
print(profit.maxProfit([7, 1, 5, 3, 6, 4]))
