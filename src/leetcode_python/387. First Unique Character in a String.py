# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = OrderedDict()
        
        for char in s:
            if char not in count_map:
                count_map[char] = 1
            else:
                count_map[char] += 1
                
        for k, v in count_map.items():
            if v == 1:
                return s.find(k)
        
        return -1
