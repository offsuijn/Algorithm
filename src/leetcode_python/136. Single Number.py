# 136. Single Number
# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using ^ operator
        ret = 0
        
        for n in nums:
            ret ^= n
        
        return ret
        
        
        # Using set()
        hashset = set()
        
        for n in nums:
            if n not in hashset:
                hashset.add(n)
            else:
                hashset.remove(n)
                
        return hashset.pop()
