# 1065번: 한수

n = int(input())

cnt = 0


def hansu(k):
    s = str(k)
    arr = [int(elem) for elem in s]  # 각 숫자를 담은 배열

    if len(arr) > 2:
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != arr[i] - arr[i - 1]:
                return False

    return True


for i in range(1, n + 1):
    if hansu(i):
        cnt += 1

print(cnt)
