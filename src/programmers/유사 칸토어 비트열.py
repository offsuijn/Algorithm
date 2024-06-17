# https://school.programmers.co.kr/learn/courses/30/lessons/148652#

def is_one(k):
    while k >= 5:
        if (k - 2) % 5 == 0:
            return False
        k //= 5
    return k != 2

def solution(n, l, r):
    cnt = 0
    for k in range(l-1, r):
        if is_one(k):
           cnt += 1
    return cnt
