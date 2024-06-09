# https://school.programmers.co.kr/learn/courses/30/lessons/148652#

def solution(n, l, r):
    answer = 0

    def f(idx):
        if idx % 5 == 2:
            return 0
        elif idx < 5:
            return 1
        else:
            return f(idx // 5)

    for i in range(l-1, r):
        answer += f(i)

    return answer
