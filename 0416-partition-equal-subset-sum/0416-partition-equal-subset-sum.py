class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If the total sum is odd, we cannot partition it into two equal subsets
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # We can always form sum 0 with an empty subset

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
