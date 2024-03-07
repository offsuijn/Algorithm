# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
      
        #Top-Down: Memoization
        def rec(n):
            if n == 0 or n ==1:
                return n
            return rec(n-1) + rec(n-2)
        
        return rec(n)

        #Bottom-Up: Tabulation
        if n == 0 or n == 1:
            return n
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
