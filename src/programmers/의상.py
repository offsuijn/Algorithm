# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter

def solution(clothes):
    answer = 1
    
    cnts = Counter([x[1] for x in clothes]).values()
    
    for c in cnts:
        answer *= (c+1)
    
    return answer-1

'''
설명!
c에 1을 더해서 곱해준 이유는 각 의상을 안 입은 경우를 추가하기 위해서 입니다.
마지막에 answer에서 1을 뺀 것은 모든 경우 중 하나도 입지 않은 경우를 제거한 것입니다.
'''
