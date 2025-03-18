from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer of the sliding window
        cur_mask = 0  # Keeps track of bitwise OR of elements in window
        max_length = 0

        for right in range(len(nums)):
            # If adding nums[right] breaks the "nice" condition, move left pointer
            while (cur_mask & nums[right]) != 0:
                cur_mask ^= nums[left]  # Remove nums[left] from the window
                left += 1  # Shrink the window from the left

            # Add nums[right] to the window
            cur_mask |= nums[right]
            
            # Update max length of the nice subarray found
            max_length = max(max_length, right - left + 1)

        return max_length
