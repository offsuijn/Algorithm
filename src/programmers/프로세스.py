# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(priorities, location):
    
    # Method 1: Trace용 Queue 생성
    queue = deque(priorities)
    trace = deque([0 for _ in range(len(priorities))])
    trace[location] = 1
    cnt = 0
    
    while queue:
        if max(trace) == 0:
            break
        if max(queue) == queue[0]:
            queue.popleft()
            trace.popleft()
            cnt += 1
        else:
            queue.append(queue.popleft())
            trace.append(trace.popleft())
            
    return cnt

    # Method 2: Priority Queue 생성
    cnt = 0
    search, s = sorted(priorities, reverse=True), 0
    
    while True:
        for i, priority in enumerate(priorities):
            cur = search[s]
            if priority == cur:
                s += 1
                cnt += 1
                if i == location:
                    break
        else: # for문을 다 돌았을 경우 다시 while문으로 간다.
            continue
        break # for문에서 break한 경우 while문도 break 한다.
    return cnt
    
    # Method 3: any 함수 사용
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    cnt = 0
    
    while queue:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            cnt += 1
            if cur[0] == location:
                return cnt
