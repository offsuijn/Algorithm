# 3197번 : 백조의 호수

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 물과 인접한 얼음을 녹인다.
def bfs_melt(r, c, lake, melt):
    next_melt = deque()  # 얼음에서 물로 바뀐 자리를 기록한다.

    while melt:
        n, m = melt.popleft()

        for i in range(4):
            nr = n + dr[i]
            nc = m + dc[i]

            # 호수를 벗어났다.
            if not (0 <= nr < r and 0 <= nc < c):
                continue

            # 얼음인 경우
            # 얼음을 물로 바꿔주고, 다음 차례 녹는 deque에 넣어준다.
            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                next_melt.append([nr, nc])

    return next_melt

# 백조가 서로 만날 수 있는지 체크한다.
def bfs_meet(r, c, lake, visited, meet):
    next_meet = deque()  # 백조가 얼음에 막힌 자리를 기록한다.

    while meet:
        n, m = meet.popleft()

        if n == swan[1][0] and m == swan[1][1]:
            return True, None

        for i in range(4):
            nr = n + dr[i]
            nc = m + dc[i]

            # 호수를 벗어났다.
            if not (0 <= nr < r and 0 <= nc < c):
                continue

            # 방문하지 않았고, 얼음인 경우
            # 방문 처리를 하고, 다음 차례 백조 deque에 넣는다.
            elif lake[nr][nc] == 'X' and not visited[nr][nc]:
                next_meet.append([nr, nc])

            # 방문하지 않았고, 물인 경우
            # 방문 처리를 하고, q에 넣는다.
            elif (lake[nr][nc] == '.' or lake[nr][nc] == 'L') and not visited[nr][nc]:
                meet.append([nr, nc])

            visited[nr][nc] = 1

    return False, next_meet


if __name__ == '__main__':
    R, C = map(int, input().split())

    lake = []  # 호수 입력 정보 저장
    swan = []  # 백조의 위치 저장

    melt = deque()  # 얼음을 녹이는 bfs에 사용되는 queue

    # 입력값 정리하기
    for r in range(R):
        row_lake = list(input().rstrip())
        for c, v in enumerate(row_lake):

            #  물이나 백조면 melt 큐에 넣는다.
            if v == '.' or v == 'L':
                melt.append([r, c])

            # 백조면 swan에 위치를 저장한다.
            if v == 'L':
                swan.append([r, c])

        # 호수 정보 저장한다.
        lake.append(row_lake)

    meet = deque()  # 백조가 만나는지 확인하는 bfs에 사용되는 queue
    n, m = swan[0][0], swan[0][1]
    meet.append([n, m])

    visited = [[0] * C for _ in range(R)]
    visited[n][m] = 1

    day = 0  # 걷잡을 수 없이 흘러가는 시간
    while True:
        day += 1

        # 얼음 녹이기
        melt = bfs_melt(R, C, lake, melt)

        isMeet, next_meet = bfs_meet(R, C, lake, visited, meet)

        if isMeet:
            print(day)
            break

        meet = next_meet
