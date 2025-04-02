from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # Not enough elements for a triplet

        # Track max_i for i < j
        max_i = nums[0]
        
        # Track max_right[k] for k > j
        max_right = [0] * n
        max_right[n-1] = nums[n-1]
        
        for k in range(n-2, -1, -1):
            max_right[k] = max(max_right[k+1], nums[k])

        max_value = 0

        for j in range(1, n-1):
            # Update max_i for the current j
            max_i = max(max_i, nums[j-1])

            # Compute triplet value
            triplet_value = (max_i - nums[j]) * max_right[j+1]

            # Update the max_value
            max_value = max(max_value, triplet_value)

        return max_value
