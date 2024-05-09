# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    
    people.sort()
    
    # Method 1: Basic Two Pointer
    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
        
    return answer

    # Method 2: Using Trick!
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            answer += 1
        right -= 1

    return len(people) - answer
