# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float('inf'), 0

        for p in prices:
            buy = min(buy, p - sell)
            sell = max(sell, p - buy - fee)

        return sell
