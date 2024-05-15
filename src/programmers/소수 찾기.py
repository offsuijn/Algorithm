# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

# Method 1: set, map, range, 그리고 permutations 함수를 멋지게 활용한 방법
def solution(n):
    primes = set()
    
    for i in range(len(n)):
        primes |= set(map(int, map("".join, permutations(list(n), i+1))))
    primes -= set(range(2)) # 0, 1 제외
    
    # 각 수가 갖는 약수는 해당 수의 제곱근을 기준으로 대칭을 이루므로 제곱근까지만 확인한다.
    for i in range(2, int((max(primes))**0.5) + 1):
        # 자기 자신은 지워지면 안 되니까 i*2부터!
        primes -= set(range(i*2, max(primes) + 1, i))
    
    return len(primes)

# Method 2: 재귀와 filter를 사용한, 기본에 충실한 방법
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
    return True

primes = set()
def permutation(base, array):
    if base:
        primes.add(int(base))
    for i, num in enumerate(array):
        permutation(base + num, array[:i] + array[i+1:])
        
def solution(n):
    permutation("", list(n))
    return len(list(filter(is_prime, primes)))
