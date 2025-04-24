class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        count = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            # Shrink the window from the left if it has all distinct elements
            while len(freq) == total_distinct:
                # All subarrays starting at `left` and ending at or after `right` are valid
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count
