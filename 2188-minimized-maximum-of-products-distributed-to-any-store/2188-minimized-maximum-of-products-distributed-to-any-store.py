from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistributeWithMax(x):
            required_stores = sum((q + x - 1) // x for q in quantities)
            return required_stores <= n
        
        # Binary search for the minimum possible x
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistributeWithMax(mid):
                right = mid
            else:
                left = mid + 1

        return left
