# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dun = len(dungeons)
    
    for permute in permutations(dungeons, dun):
        hp = k
        cnt = 0
        
        for p in permute:
            if hp >= p[0]:
                hp -= p[1]
                cnt += 1
            
            if cnt > answer:
                answer = cnt
    
    return answer
