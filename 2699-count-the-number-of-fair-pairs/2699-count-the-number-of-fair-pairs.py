class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1):
            # Find left bound for nums[i] + nums[j] >= lower
            left_bound = bisect_left(nums, lower - nums[i], i + 1)
            # Find right bound for nums[i] + nums[j] <= upper
            right_bound = bisect_right(nums, upper - nums[i], i + 1) - 1
            # Count valid pairs in the range [left_bound, right_bound]
            if left_bound <= right_bound:
                count += right_bound - left_bound + 1
        return count

        