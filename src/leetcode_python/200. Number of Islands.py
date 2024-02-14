# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        islands = 0

        def explore(r,c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    grid[r][c] = "0"
                    for i, j in dir:
                        explore(r+i, c+j)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    explore(r,c)
        return islands
