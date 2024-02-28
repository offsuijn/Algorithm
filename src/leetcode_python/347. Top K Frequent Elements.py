# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Count.most_common()
        cnt = Counter(nums)
        return [n for n, _ in cnt.most_common(k)]
        
        # Use heqpq.nlargest()
        if k ==len(nums):
            return nums
        
        count = collections.Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key=count.get)
