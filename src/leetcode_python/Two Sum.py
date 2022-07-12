# 1번 : Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for idx, i in enumerate(nums):
            if (target - i) in nums:
                j = nums.index(target - i)
                if idx != j:
                    result = [idx, j]
                    break
                    
        return result
