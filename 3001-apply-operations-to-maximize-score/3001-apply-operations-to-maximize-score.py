from typing import List
from collections import defaultdict
import heapq

class Solution:
    def count_prime_factors(self, n: int) -> int:
        """Returns the number of distinct prime factors of n."""
        i, count = 2, 0
        original_n = n
        while i * i <= n:
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:  # If n itself is prime
            count += 1
        return count

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Compute prime scores for each number in nums
        prime_scores = [self.count_prime_factors(num) for num in nums]

        # Step 2: Determine range contribution for each element
        left = [0] * n
        right = [n - 1] * n
        stack = []

        # Monotonic Stack (Next Smaller Element to the Left)
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        stack.clear()

        # Monotonic Stack (Next Smaller Element to the Right)
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)

        # Step 3: Store (effect, value) pairs
        contributions = []
        for i in range(n):
            effect = (i - left[i] + 1) * (right[i] - i + 1)
            contributions.append((nums[i], effect))

        # Step 4: Maximize score using a heap
        contributions.sort(reverse=True, key=lambda x: x[0])  # Sort by value (descending)
        score = 1

        for num, effect in contributions:
            if k <= 0:
                break
            use = min(effect, k)
            score = (score * pow(num, use, MOD)) % MOD
            k -= use

        return score
