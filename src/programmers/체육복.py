# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    l1 = set(lost)
    l2 = set(reserve)
    lost = list(l1 - l2)
    reserve = list(l2 - l1)
    
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            n -= 1
    
    return n
