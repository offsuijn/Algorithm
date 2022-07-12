# 125. Valid Palindrome

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        풀이 1 : 뒤집어서 비교
        1. s에서 alpha OR num을 추출하여 input 리스트를 만든다.
        2. input을 거꾸로 뒤집어서 input_reverse를 만든다.
        3. input과 input_reverse가 같은지 확인한다.
        """
        
        input = [e.lower() for e in s if e.isalnum()]
        input_reverse = input[:]
        input_reverse.reverse()
        input = ''.join(input)
        input_reverse = ''.join(input_reverse)
        
        return input == input_reverse
    
        """
        풀이 2 : 정규식 사용
        1. s를 소문자로 변환하고, 정규식을 사용하여 alpha와 num만 남긴다.
        2. 뒤집어서 동일한지 확인한다.
        """
        
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)
        return s == s[::-1]
