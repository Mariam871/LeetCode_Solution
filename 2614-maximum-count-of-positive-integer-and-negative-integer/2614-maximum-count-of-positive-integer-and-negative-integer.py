class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = bisect_right(nums, -1)  # Count of negative numbers
        pos_count = len(nums) - bisect_left(nums, 1)  # Count of positive numbers
        return max(neg_count, pos_count)  # Return the maximum of both