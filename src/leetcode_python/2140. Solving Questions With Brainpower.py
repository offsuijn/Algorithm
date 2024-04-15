# https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            hop = min(n, i + questions[i][1] + 1)
            dp[i] = max(questions[i][0] + dp[hop], dp[i+1])

        return dp[0]
