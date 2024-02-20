# 599. Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
            
        words1 = {s: i for i, s in enumerate(list1)}
        for i, s in enumerate(list2):
            if s in words1:
                common[s] = words1[s] + i
        
        ret = []
        min_index = float("inf")
        for s, i in common.items():
            if i < min_index:
                min_index = i
                ret.clear()
                ret.append(s)
            elif i == min_index:
                ret.append(s)

        return ret
