# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while True:
        first = heapq.heappop(scoville)
        
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, second * 2 + first)
        cnt += 1

    return cnt
