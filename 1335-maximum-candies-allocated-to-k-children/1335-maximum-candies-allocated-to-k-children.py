from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0

        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)

            if count >= k:
                result = mid  # Store the current mid as a possible answer
                left = mid + 1  # Try for a larger value
            else:
                right = mid - 1  # Try for a smaller value

        return result

