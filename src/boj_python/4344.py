# 4344번: 평균은 넘겠지

c = int(input())

for _ in range(c):
    in_arr = list(map(int, input().split()))
    n = in_arr[0]
    arr = [in_arr[i] for i in range(1, n+1)]

    avg = sum(arr) / n
    cnt = 0
    for elem in arr:
        if elem > avg:
            cnt += 1
    print(f"{(cnt*100)/n:.3f}%")
