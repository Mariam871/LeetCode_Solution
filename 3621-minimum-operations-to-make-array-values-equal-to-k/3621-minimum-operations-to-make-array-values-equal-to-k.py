from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Step 1: If any number is less than k, we can never increase it → impossible
        if any(num < k for num in nums):
            return -1

        # Step 2: Count frequency of each value in nums
        freq = Counter(nums)

        # Step 3: Extract all unique values >= k and sort descending
        unique_vals = sorted([val for val in freq if val >= k], reverse=True)

        operations = 0

        # Step 4: Move from top value down to k
        for i in range(1, len(unique_vals)):
            higher_val = unique_vals[i - 1]
            lower_val = unique_vals[i]

            # Check if all nums > lower_val are equal to higher_val → valid h
            if all(num == higher_val for num in nums if num > lower_val):
                operations += 1
                # Reduce all values > lower_val to lower_val
                nums = [min(num, lower_val) for num in nums]
            else:
                return -1

        # Finally, if last value is not yet k, one more operation needed
        if unique_vals[-1] != k:
            # Check if h = k is valid
            if all(num == unique_vals[-1] for num in nums if num > k):
                operations += 1
                nums = [min(num, k) for num in nums]
            else:
                return -1

        return operations
