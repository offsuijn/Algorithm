# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque
def solution(order):
    main = deque([i for i in range(1, len(order) + 1)])
    sub = []
    cnt = 0
    
    for target in order:
        # Find the target box from main container belt
        if main and main[0] <= target:
            while main[0] < target:
                sub.append(main.popleft())
            main.popleft()
            cnt += 1
            continue
        
        # Find the target box from sub container belt
        if sub and sub[-1] == target:
            sub.pop()
            cnt += 1
            continue
            
        # Cannot find the target box
        break
    
    return cnt
