# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    cnt = [0] * 3

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, ans in enumerate(answers):
        if ans == supo1[idx % len(supo1)]:
            cnt[0] += 1
        if ans == supo2[idx % len(supo2)]:
            cnt[1] += 1
        if ans == supo3[idx % len(supo3)]:
            cnt[2] += 1
    
    for idx, val in enumerate(cnt):
        if val == max(cnt):
            answer.append(idx+1)
    
    return answer
