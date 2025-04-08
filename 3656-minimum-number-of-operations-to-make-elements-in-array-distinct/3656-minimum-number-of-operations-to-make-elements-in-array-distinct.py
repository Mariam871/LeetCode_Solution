class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Try removing 0 to max possible operations (ceil(n / 3))
        for ops in range((n + 2) // 3 + 1):
            start = ops * 3
            remaining = nums[start:]
            if len(set(remaining)) == len(remaining):
                return ops
        return (n + 2) // 3  # If no distinct suffix found, remove all
