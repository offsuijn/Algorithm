# https://leetcode.com/problems/combination-sum-iv/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
    
        for i in range(1, target+1):
            for n in nums:
                if i-n >= 0:
                    dp[i] += dp[i-n]
        
        return dp[-1]
