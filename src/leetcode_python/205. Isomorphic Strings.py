# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        hashmap = {}
        
        for i, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = t[i]
            elif hashmap[char] != t[i]:
                return False
        return True
