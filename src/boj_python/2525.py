# 2525번: 오븐 시계

h, m = map(int, input().split())
n = int(input())

n_h = n // 60
n_m = n % 60

m += n_m # 분 더하기
n_h += m//60
m %= 60

h += n_h # 시 더하기
if h > 23:
  h -= 24

print(h, m)
