# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=dynamic-programmingv

from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Memoization - TopDown
        @lru_cache
        def dfs(i, j):
            if i >= m or j >= n: # exceed
                return 0
            
            if obstacleGrid[i][j]: # hit an obstacle
                return 0

            if i == m-1 and j == n-1: # meet the end
                return 1

            return dfs(i+1, j) + dfs(i, j+1)

        return dfs(0, 0)

        # Tabulation - BottomUP
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m) :
            for j in range(n) :
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                if i==0:
                    dp[i][j] = dp[i][j-1]
                    continue
                if j==0:
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
