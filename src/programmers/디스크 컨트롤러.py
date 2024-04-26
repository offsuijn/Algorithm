# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque

def solution(jobs):
    heap = []
    total = 0 # 각 작업이 소요한 시간의 합
    time = 0 # 시간
    
    # 작업이 요청되는 시점, 작업의 소요시간 순서로 정렬한 task
    task = deque(sorted([(x[0], x[1]) for x in jobs], key=lambda x: (x[0], x[1])))

    while task or heap:
        # 대기자 있을 경우 heap부터
        if heap:
            job = heapq.heappop(heap)
            arrived, duration = job[1], job[0]
        else:
            job = task.popleft()
            arrived, duration = job[0], job[1]
        
        time = max(time + duration, arrived + duration)
        total += time - arrived
        
        # 대기자 heap으로 이동
        while task:
            if task[0][0] > time:
                break
            job = task.popleft()
            heapq.heappush(heap, (job[1], job[0])) # 소요 시간 기준으로 정렬
        
    return total // len(jobs)
