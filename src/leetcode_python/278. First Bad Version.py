# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int) -> int:

    
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            isBad = isBadVersion(mid)
            if(isBad):
                right = mid-1
            else:
                left = mid+1
                
        return left
