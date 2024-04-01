# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, cooldown, sell = float('inf'), 0, 0

        for p in prices:
            buy = min(buy, p - cooldown)
            cooldown = sell
            sell = max(sell, p - buy)

        return sell
