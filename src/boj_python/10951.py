# 10951번: A+B -4

# 풀이 1 : EOFError
while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except EOFError:
    break
    
# 풀이 2 : readlines()
import sys

lines = sys.stdin.readlines()

for line in lines:
  a, b = map(int, line.split())
  print(a+b)
