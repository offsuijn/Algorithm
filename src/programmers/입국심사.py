# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    left = times[0]
    right = times[0] * n
    
    # n = target, cnt = mid
    while(left < right):
        cnt = 0
        mid = (left + right) // 2
        
        for t in times:
            cnt += (mid // t)
        
        if (n <= cnt): # lower_bound
            right = mid
        else:
            left = mid + 1
        
    return right
