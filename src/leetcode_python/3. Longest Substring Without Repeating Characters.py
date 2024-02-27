# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use List
        max_length = 0
        curr_str = []
        l = 0
        
        for r, char in enumerate(s):
            if char in curr_str:
                if (r - l) > max_length:
                    max_length = (r - l)
                l += (curr_str.index(char) + 1)
                curr_str = curr_str[curr_str.index(char)+1:]
            curr_str.append(char)
                
                
        return max_length if max_length > len(curr_str) else len(curr_str)
    
        # Use Hashmap
        found = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char not in found:
                found[char] = right
            else:
                if found[char] < left:
                    found[char] = right # curr_string 이전에 found된 char이므로 무시하고 index만 업데이트한다.
                else:
                    left = found[char] + 1
                    found[char] = right
            max_length = max(max_length, (right - left + 1))
            
        return max_length
