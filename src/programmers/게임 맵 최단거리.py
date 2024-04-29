# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        x, y, d = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < m and ny < n and maps[ny][nx] == 1:
                    maps[ny][nx] = 0 # 방문 처리
                    queue.append((nx, ny, d + 1))

    return -1
