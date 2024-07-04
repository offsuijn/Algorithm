# https://www.acmicpc.net/problem/7579

import sys

n, m = map(int, sys.stdin.readline().split())
memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(n+1)]
answer = int(1e9)

for i in range(1, n+1):
    for j in range(sum(cost)+1):
        cur_memory = memory[i]
        cur_cost = cost[i]

        if (j < cost[i]):
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j-cur_cost] + cur_memory, dp[i-1][j])

        if (dp[i][j] >= m):
            answer = min(answer, j)

print(answer)
