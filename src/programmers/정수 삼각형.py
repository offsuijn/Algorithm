# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):
            left = triangle[i-1][j-1] if j-1 >= 0 else 0
            right = triangle[i-1][j] if j < i else 0
            triangle[i][j] += max(left, right)

    return max(triangle[-1])
