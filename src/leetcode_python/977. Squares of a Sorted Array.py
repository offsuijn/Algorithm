# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            ans.append(n*n)

        ans.sort()
        return ans
