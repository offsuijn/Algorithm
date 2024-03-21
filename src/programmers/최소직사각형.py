# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    width = max(sizes[0])
    height = min(sizes[0])
    
    for w, h in sizes:
        if (width >= w and height >= h) or (width >= h and height >= w):
            continue
        width = max(max(w, h), width)
        height = max(min(w, h), height)
        
        
    return width*height
    
    # 1 linear
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
