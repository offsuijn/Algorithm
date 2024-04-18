# https://school.programmers.co.kr/learn/courses/30/lessons/42586#qna

import math

def solution(progresses, speeds):
    answer = []
    days = []
    n = len(progresses)

    # Method1 for making days
    for i in range(n):
        days.append(math.ceil((100-progresses[i]) / speeds[i]))
    # Method2 for making days
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    
    cnt = 1
    d = days[0]
    for i in range(1, n):
        if d >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            d = days[i]
        
    answer.append(cnt)
    return answer
