# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N+1)

        dp[0] = dp[1] = 0
        for i in range(2, N+1):
            # i-2에서 돈 내고 2계단 올라온 경우 vs. i-1에서 돈 내고 1계단 올라온 경우
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[N]
