# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        
        while n != 1:
            if n in hashset:
                return False
            hashset.add(n)
            
            sum = 0
            while n != 0:
                rem = n % 10
                sum += rem**2
                n //= 10
            
            n = sum
        
        return True
