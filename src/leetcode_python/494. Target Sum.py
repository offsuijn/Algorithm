# 494. Target Sum
# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def explore(curr: int, nums: List[int]):
            key = (curr, tuple(nums))
            if key in cache:
                return cache[key]
            
            if not nums:
                return 1 if curr == target else 0
            
            ans = explore(curr+nums[0], nums[1:]) + explore(curr-nums[0], nums[1:])
            cache[key] = ans
            return ans
        
        cache = {}
        return explore(0, nums)
