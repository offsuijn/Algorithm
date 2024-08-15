# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict 

def dfs(graph, N, key, footprint):
    
    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx) # idx를 기억해두고 dfs 호출 전후로 pop, insert

        tmp = footprint[:] # dfs 태울 복사본
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country) # 호출 후 graph 원상복구

        if ret: # 탐색이 끝나지 않은 경우 None 반환 -> 루프 차단
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)
    N = len(tickets)
    
    for t in tickets:
        graph[t[0]].append(t[1])
        graph[t[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer
