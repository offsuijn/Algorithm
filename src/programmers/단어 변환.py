# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
def solution(begin, target, words):
    
    def changeable(word, target):
        cnt = 0
        for w, t in zip(word, target):
            if w != t:
                cnt += 1
                if cnt > 1:
                    return False
        
        return True if cnt == 1 else False
    
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((words, begin, 0))
    
    while queue:
        words, word, cnt = queue.popleft()
        for w in words:
            if changeable(word, w):
                if w == target:
                    return cnt+1
                words.remove(w)
                if not words:
                    return 0
                queue.append((words, w, cnt+1))

    return 0
