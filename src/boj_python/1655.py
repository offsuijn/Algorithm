# 1655번: 가운데를 말해요

import heapq
import sys

input = sys.stdin.readline

N = int(input())
left_h = []  # 최대힙, 첫번째 원소는 항상 중간값이다.
right_h = []  # 최소힙

for i in range(N):
    num = int(input())

    # 숫자의 개수가 짝수면 왼쪽에 넣고 홀수이면 오른쪽에 넣는다.
    if i % 2 == 0:
        heapq.heappush(left_h, -num)
    else:
        heapq.heappush(right_h, num)

    # 오른쪽에 원소가 있고, 왼쪽의 최댓값보다 오른쪽의 최솟값이 작은 경우 둘을 바꿔준다.
    if right_h and (-left_h[0] > right_h[0]):
        min_value = heapq.heappop(right_h)
        max_value = -heapq.heappop(left_h)

        heapq.heappush(right_h, max_value)
        heapq.heappush(left_h, -min_value)

    # 중간값을 출력한다.
    print(-left_h[0])
