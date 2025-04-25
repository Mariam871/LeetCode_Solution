class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        freq = defaultdict(int)
        freq[0] = 1  # for subarrays starting at index 0
        result = 0

        for num in nums:
            # Increment prefix count if condition is met
            if num % modulo == k:
                prefix_count += 1

            # Calculate target mod value for valid subarray
            target = (prefix_count - k) % modulo

            # Add number of previous prefix sums that match the target
            result += freq[target]

            # Record the current prefix sum modulo
            freq[prefix_count % modulo] += 1

        return result
