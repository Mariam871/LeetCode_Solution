class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(cap):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip the next house after robbing
                i += 1
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid  # Try to minimize capability
            else:
                left = mid + 1  # Increase capability
        return left
