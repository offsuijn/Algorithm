# https://leetcode.com/problems/delete-and-earn/submissions/1200517122/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        reduced = [0] * (max(nums) + 1)
        for n in nums:
            reduced[n] += n

        dp = [0] * len(reduced)
        dp[1] = reduced[1]
        for i in range(2, len(reduced)):
            dp[i] = max(dp[i-1], dp[i-2] + reduced[i])

        return dp[-1]
