# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
    
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n > 0:
            if n % 2 == 0:
                return self.myPow(x * x, n // 2)
            else: 
                return self.myPow(x * x, n // 2) * x
