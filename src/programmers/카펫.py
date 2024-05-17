# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    summ = brown + yellow
    candidates = [(w, summ//w) for w in range(3, int(summ**0.5)+1) if summ % w == 0]
    
    for w, h in candidates:
        if (w-2) * (h-2) == yellow:
            return [w, h] if w >= h else [h, w]
