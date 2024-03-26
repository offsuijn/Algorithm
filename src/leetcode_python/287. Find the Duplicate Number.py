https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Counter
        return Counter(nums).most_common(1)[0][0]

        # Use Set
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
