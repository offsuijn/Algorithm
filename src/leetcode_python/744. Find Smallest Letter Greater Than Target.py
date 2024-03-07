# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Use Binary Search
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return letters[left] if letters[left] > target else letters[0]
    
        # Use Iteration
        for l in letters:
            if l > target:
                return l
        return letters[0]
