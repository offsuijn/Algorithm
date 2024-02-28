# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
            elif res == 0:
                return mid
