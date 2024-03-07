# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# Use cnt as local variable
def solution(numbers, target):
    dirs = (-1, +1)
    N = len(numbers)
    cnt = 0
    
    # i = 현재 index, num = 지난 값의 합
    def find(i, num):
        if i == N and num == target:
            nonlocal cnt
            cnt += 1
        elif i == N:
            return 
        
        for d in dirs:
            find(i+1, num + d*numbers[i])

    find(0, 0)
    return cnt

# Use cnt as global variable
cnt = 0
def solution(numbers, target):
    dirs = (-1, +1)
    N = len(numbers)
    global cnt
    
    # i = 현재 index, num = 지난 값의 합
    def find(i, num):
        if i == N and num == target:
            # cnt -> UnboundLocalError
            # nonlocal cnt -> SyntaxError
            global cnt
            cnt += 1
            return
        elif i == N:
            return 
        
        for d in dirs:
            find(i+1, num + d*numbers[i])

    find(0, 0)
    return cnt
