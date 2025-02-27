from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}  # Map value to index
        dp = {}  # Dictionary to store (i, j) -> length of Fibonacci-like sequence
        max_len = 0

        for j in range(len(arr)):
            for i in range(j):
                x = arr[j] - arr[i]  # Find previous number in sequence
                if x in index and index[x] < i:  # Ensure x exists before i
                    k = index[x]
                    dp[i, j] = dp.get((k, i), 2) + 1  # Default to 2 if not found
                    max_len = max(max_len, dp[i, j])

        return max_len if max_len >= 3 else 0  # Return 0 if no valid sequence found
