# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    n = len(money)
    
    dp1 = [0] * n
    dp2 = [0] * n
    
    # 첫 집을 털었을 경우
    dp1[0], dp1[1] = money[0], money[0]
    
    # 첫 집을 털지 않고, 두번째 집을 털었을 경우
    dp2[0], dp2[1] = 0, money[1]
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        
    last = n-1
    
    # 첫 집을 털었으므로, 마지막 집은 털 수 없다.
    dp1[n-1] = dp1[last - 1]
    
    # 첫 집을 털지 않았으므로, 마지막 집을 털 수 있다.
    dp2[n-1] = max(dp2[last - 1], dp2[last - 2] + money[last])

    return max(dp1[-1], dp2[-1])
