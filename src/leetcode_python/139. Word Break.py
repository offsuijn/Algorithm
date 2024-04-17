# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for r in range(1, n + 1):
            for l in range(r):
                if dp[l] and s[l:r] in wordDict:
                    dp[r] = True
                    break
                    
        return dp[-1]
