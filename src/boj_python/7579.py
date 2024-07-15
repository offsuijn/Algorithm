# https://www.acmicpc.net/problem/7579

n, m = map(int, input().split()) # n = 활성화된 앱의 개수, m = 필요한 바이트
memory = list(map(int, input().split())) # 앱이 사용 중인 메모리
costs = list(map(int, input().split())) # 앱을 비활성화할 때의 비용

dp = [0] * (sum(costs)+1)

answer = sum(costs)
for i in range(n):
    for j in range(sum(costs), -1, -1): # 역순으로 순회, 0도 cost 가능!!
        if j >= costs[i]:
            dp[j] = max(dp[j], dp[j-costs[i]]+memory[i])

        if dp[j] >= m:
            answer = min(answer, j)
            
print(answer)
