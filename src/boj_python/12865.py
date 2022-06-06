'''
12865번: 평범한 배낭
=> dp문제
'''

import sys

N, K = tuple(map(int, sys.stdin.readline().split()))  # 물품의 수, 버틸 수 있는 무게
w_arr =[0]*(N+1)
v_arr = [0]*(K+1)

for i in range(1, N+1):
    w_arr[i], v_arr[i] = tuple(map(int, sys.stdin.readline().split())) # 물건의 무게와 가치 초기화

dp_arr = [[0]*(K+1) for _ in range(N+1)]

max_value = -sys.maxsize  # 가치합의 최댓값

for i in range(1, N+1):
    for j in range(1, K+1):

        if w_arr[i] > j:  # 현재 물건의 무게가 배낭무게보다 크면
            dp_arr[i][j] = dp_arr[i-1][j]  # 이전 물건을 담을 때까지의 가치합을 저장

        else:  # 이전 물건을 담을 때까지의 가치합 vs 내 물건을 담을 공간을 남긴만큼의 이전 가치합과 + 현재 물건 가치합
            dp_arr[i][j] = max(dp_arr[i-1][j], dp_arr[i-1][j-w_arr[i]]+v_arr[i])

    if dp_arr[i][K] > max_value:
        max_value = dp_arr[i][K]

print(max_value)
