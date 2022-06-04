'''
1003번: 피보나치 함수
-> 0과 1의 호출횟수도 피보나치 수열을 따른다!
'''

T = int(input())

# 0과 1 호출 횟수를 담은 배열
zero_arr = [1, 0, 1]
one_arr = [0, 1, 1]

for _ in range(T):
    n = int(input())

    if len(zero_arr) < n + 1:
        for i in range(len(zero_arr), n + 1):
            # 0과 1에 피보나치 수 적용하기
            zero_arr.append(zero_arr[i - 2] + zero_arr[i - 1])
            one_arr.append(one_arr[i - 2] + one_arr[i - 1])

    print(f"{zero_arr[n]} {one_arr[n]}")
