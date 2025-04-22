class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # Precompute all divisors
        divisors = [[] for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            for j in range(2 * i, maxValue + 1, i):
                divisors[j].append(i)

        # dp[k][v] = number of sequences of length k ending with value v
        max_len = min(14, n)  # beyond this length, sequences are rare
        dp = [defaultdict(int) for _ in range(max_len + 1)]
        
        for v in range(1, maxValue + 1):
            dp[1][v] = 1

        for k in range(2, max_len + 1):
            for v in range(1, maxValue + 1):
                for d in divisors[v]:
                    dp[k][v] = (dp[k][v] + dp[k - 1][d]) % MOD

        # Precompute combinations C(n-1, k-1)
        combs = [1] * (max_len + 1)
        for k in range(2, max_len + 1):
            combs[k] = comb(n - 1, k - 1) % MOD

        # Sum total number of valid arrays
        result = 0
        for k in range(1, max_len + 1):
            for v in dp[k]:
                result = (result + dp[k][v] * combs[k]) % MOD

        return result
