from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        # Store the product frequencies
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1  # Count the number of pairs for each product

        # Count valid tuples
        result = 0
        for count in product_count.values():
            if count > 1:
                result += 8 * (count * (count - 1) // 2)  # Each valid pair gives 8 permutations

        return result