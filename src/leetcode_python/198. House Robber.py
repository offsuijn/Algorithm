# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        dp = [0] * N

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
