# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Use Set
        jewel_set = set()
        cnt = 0
        
        for j in jewels:
            jewel_set.add(j)
            
        for s in stones:
            if s in jewel_set:
                cnt += 1
                
        return cnt
    
        # Use list.count()
        jewel_count = 0

        for jewel in jewels:
            jewel_count += stones.count(jewel)

        return jewel_count
