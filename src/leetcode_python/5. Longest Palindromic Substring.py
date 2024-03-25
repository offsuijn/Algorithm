# https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        answer = s[0]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        if len(answer) < j-i+1:
                            answer = s[i:j+1]

        return answer
