class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        left = 0
        max_beauty = 0

        # Step 2: Sliding window to find the maximum subsequence length
        for right in range(len(nums)):
            # Ensure the range [nums[left], nums[right]] is valid (difference <= 2k)
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # Update the maximum beauty (length of the valid subsequence)
            max_beauty = max(max_beauty, right - left + 1)

        return max_beauty