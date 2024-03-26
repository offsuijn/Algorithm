# https://leetcode.com/problems/coin-change-ii/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        
        return dp[-1]
