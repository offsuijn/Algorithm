# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return sqrt(num)==floor(sqrt(num))
        
        left = 0
        right = N = num
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid == 0:
                return True
            
            res = N / mid
            if res == mid:
                return True
            elif res > mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
