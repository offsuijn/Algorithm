# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    type = set()
    N = len(nums)
    
    for n in nums:
        if n not in type:
            type.add(n)
    if len(type) > (N / 2):
        return (N / 2)
    else:
        return len(type)
    
    # One-Liner Challenge
    return min(len(nums)/2, len(set(nums)))
