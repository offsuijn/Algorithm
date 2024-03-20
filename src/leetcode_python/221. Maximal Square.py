# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, result = len(matrix), len(matrix[0]), 0
      
        dp = [0] * n
        for i in range(m):
            prev = 0
            for j in range(n):
                dp[j], prev = 0 if matrix[i][j] == '0' else (min(dp[j], dp[j-1] if j > 0 else 0, prev)+ 1), dp[j]
                result = dp[j] if dp[j] > result else result
        return result * result
