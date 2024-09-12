class Solution:
    def predictTheWinner(self, nums):  # Change method name to match the expected one
        n = len(nums)
        # Create a 2D DP array initialized to 0
        dp = [[0] * n for _ in range(n)]

        # Base case: when there's only one number left
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill the DP table
        for length in range(2, n + 1):  # subarray lengths from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        # Player 1 can win if the score difference is >= 0
        return dp[0][n-1] >= 0

# Example of calling the solution (if you are manually testing it):
param_1 = [1, 5, 2]
ret = Solution().predictTheWinner(param_1)  # Now using the correct lowercase method name
print(ret)
