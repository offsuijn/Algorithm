# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        # Use Array
        result = []
        for idx, i in enumerate(nums):
            if (target - i) in nums:
                j = nums.index(target - i)
                if idx != j:
                    result = [idx, j]
                    break
                    
        return result

        # Use HashMap
        hashmap = {}
        
        for i, n in enumerate(nums):
            if target - n in hashmap:
                return hashmap[target-n], i
            
            hashmap[n] = i
