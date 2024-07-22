# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    matrix =  [ [ 0 for _ in range(n+1) ] for _ in range(n+1) ]
    for (win, lose) in results: matrix[win][lose],matrix[lose][win] = win,win

    for _ in range(2):
        for win in range(1,n+1):
            for lose in range(1,n+1):
                if win == matrix[win][lose]:
                    for i, j in enumerate(matrix[lose]):
                        if j == lose: matrix[win][i],matrix[i][win] = win,win

    for i in range(1, n+1):
        if matrix[i].count(0)-1 == 1: answer += 1

    return answer
