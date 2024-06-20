# https://school.programmers.co.kr/learn/courses/30/lessons/12936#

import math
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    
    while n > 0:
        answer.append(nums.pop((k-1) // math.factorial(n-1)))
        n, k = n-1, k%math.factorial(n-1)
    
    return answer
