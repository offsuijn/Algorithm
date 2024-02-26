# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/description/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        nums12_map = defaultdict(int)
        ans = 0
        
        for i in nums1:
            for j in nums2:
                nums12_map[i+j] += 1
        
        for k in nums3:
            for l in nums4:
                ans += nums12_map[-(k+l)]
        
        return ans
