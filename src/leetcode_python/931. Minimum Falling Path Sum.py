# https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        for i in range(1, M):
            for j in range(N):
                a = matrix[i-1][j-1] if 0 < j else float('inf')
                b = matrix[i-1][j]
                c = matrix[i-1][j+1] if j < N - 1 else float('inf')
                matrix[i][j] += min(a, b, c)
        return min(matrix[-1])
