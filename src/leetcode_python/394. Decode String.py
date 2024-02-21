# 394. Decode String
# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = collections.deque()
        ans = []
        curr_str = ''
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_str = ''
                curr_num = 0
            elif char == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += char
                
        return curr_str
