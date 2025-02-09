from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        good_pairs = 0
        n = len(nums)

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq_map[key]  # Count pairs with same key
            freq_map[key] += 1  # Update frequency

        total_pairs = (n * (n - 1)) // 2
        return total_pairs - good_pairs
