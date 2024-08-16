# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = []
    
    for idx, p in enumerate(prices):
        while stack and stack[-1][1] > p: # 가격이 떨어진 경우
            t_idx, t_p = stack.pop()
            answer[t_idx] = idx - t_idx
        stack.append((idx, p))
    
    while stack:
        idx, p = stack.pop()
        answer[idx] = (N-1) - idx
    
    return answer
