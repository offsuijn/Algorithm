# 2636번 : 치즈

import sys
from collections import deque

cheese = []
ans = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append([0, 0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    melt_cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if not cheese[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1
            elif cheese[nx][ny] and not visited[nx][ny]:
                cheese[nx][ny] = 0
                visited[nx][ny] = 1
                melt_cnt += 1
    return melt_cnt


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    for _ in range(n):
        cheese.append(list(map(int, input().split())))

    time = 0
    while True:
        cnt = bfs()
        if cnt == 0:
            print(time)
            print(ans[-1])
            break
        time += 1
        ans.append(cnt)
