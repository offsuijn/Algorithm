# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use HashMap
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        cnt = Counter(nums1)
        ans = []
        
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        
        return ans
    
        # Use Sort & Two Pointers
        
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums[i])
                i += 1
                j += 1
                
        return ans
