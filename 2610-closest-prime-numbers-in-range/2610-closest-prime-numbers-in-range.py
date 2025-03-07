from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Use the Sieve of Eratosthenes to find primes up to `right`
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime

        # Generate primes up to 'right'
        primes = sieve(right)

        # Step 2: Collect all primes in the range [left, right]
        prime_list = [i for i in range(left, right + 1) if primes[i]]

        # Step 3: Find the closest pair of primes
        if len(prime_list) < 2:
            return [-1, -1]

        min_gap = float('inf')
        result = [-1, -1]

        for i in range(len(prime_list) - 1):
            num1, num2 = prime_list[i], prime_list[i + 1]
            if num2 - num1 < min_gap:
                min_gap = num2 - num1
                result = [num1, num2]

        return result
