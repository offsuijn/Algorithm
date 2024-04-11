# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    def dfs(visited, computers, i):
        visited[i] = 1
        for j in range(n):
            if i != j and visited[j] == 0 and computers[i][j] == 1:
                dfs(visited, computers, j)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(visited, computers, i)
            answer += 1
            
    return answer
