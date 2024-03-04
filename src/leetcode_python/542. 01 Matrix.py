# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/description/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Set queue with 0s and set else to max_value
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        
        while queue:
            i, j = queue.popleft()
            for r, c in directions:
                new_r, new_c = i+r, j+c
                
                if 0 <= new_r < m and 0 <= new_c < n and mat[new_r][new_c] > mat[i][j] + 1:
                    # the shortest distance of each cell to the nearest 0
                    mat[new_r][new_c] = mat[i][j] + 1
                    queue.append((new_r, new_c))
                    
                    
        return mat
