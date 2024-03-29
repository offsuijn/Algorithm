# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = inf, 0

        for p in prices:
            buy = min(buy, p - sell)
            sell = max(sell, p - buy)

        return sell
