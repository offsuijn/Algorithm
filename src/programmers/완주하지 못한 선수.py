# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# Using Counter
from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    
    non = part - comp # - 연산 -> 0 또는 음수 제거
    # part.subtract(comp) # subtract -> 0 또는 음수 포함
    
    return ''.join(non.elements()) # elements() -> 0 또는 음수 제거
