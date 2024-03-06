# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque

def solution(arr):
    answer = []
    
    for num in arr:
        if answer[-1:] == [num]: 
            continue
        answer.append(num)
    return answer
