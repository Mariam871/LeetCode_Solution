from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # One extra space for convenience

        for i in range(n - 1, -1, -1):  # Iterate backwards
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            dp[i] = max(points + (dp[next_q] if next_q < n else 0), dp[i + 1])

        return dp[0]  # Return the maximum points from index 0
