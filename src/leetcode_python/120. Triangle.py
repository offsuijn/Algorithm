# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)

        # Top-down
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                    continue
                if j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                    continue

                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[n-1])

        # Bottom-up
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min([triangle[i+1][j], triangle[i+1][j+1]])
        return triangle[0][0]
