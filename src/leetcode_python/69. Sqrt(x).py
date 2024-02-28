# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        nearest = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid < x:
                left = mid + 1
                nearest = mid
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
            
        return nearest
