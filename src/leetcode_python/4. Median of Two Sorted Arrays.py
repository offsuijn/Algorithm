# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Method1: Make them merged by myself
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid] + merged[mid-1]) / 2
        else:
            return merged[mid]

        # Method2: Use sorted() method
        merged = sorted(nums1 + nums2)
        n = len(merged)

        mid = n // 2
        if n % 2 == 0:
            return (merged[mid]+merged[mid-1]) / 2
        else:
            return merged[mid]
