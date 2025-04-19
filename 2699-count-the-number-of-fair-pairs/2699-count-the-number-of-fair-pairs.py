class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            left = lower - nums[i]
            right = upper - nums[i]
            # Use binary search to find the range of valid pairs (j > i)
            low_idx = bisect_left(nums, left, i + 1)
            high_idx = bisect_right(nums, right, i + 1)
            count += (high_idx - low_idx)
        
        return count
