# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        curr, prev = [0]*n, [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    curr[j] = min(curr[j-1] if j > 0 else 0,
                                prev[j],
                                prev[j-1] if j > 0 else 0) + 1
                else:
                    curr[j] = 0 # reset curr[j]
                if result < curr[j]:
                    result = curr[j]
            prev, curr = curr, prev
        
        return result*result
