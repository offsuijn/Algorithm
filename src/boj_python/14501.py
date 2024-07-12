# https://www.acmicpc.net/problem/14501

n = int(input())

schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if (i + schedule[i][0]) <= n: # 스케줄을 선택할 경우
        dp[i] = max(dp[i+1], dp[i + schedule[i][0]] + schedule[i][1])
    else: # 스케줄을 선택하지 않을 경우
        dp[i] = dp[i+1]

print(dp[0])
