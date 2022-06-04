# 1157번: 단어 공부

import sys

s = input()
s = s.upper()

# 알파벳 개수 크기의 배열 생성
ascii_arr = [0] * (ord('Z') - ord('A') + 1)

# 각 알파벳 개수 세기
for i in s:
    ascii_arr[ord(i) - ord('A')] += 1

max_cnt = max(ascii_arr)
max_idx = ascii_arr.index(max_cnt)

# 가장 많이 사용된 알파벳 중복 검사
if max_cnt in ascii_arr[(max_idx + 1):]:
    print("?")
    sys.exit()

print(chr(max_idx + ord('A')))
