class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):  # Ensure we have at least 3 elements to flip
            if nums[i] == 0:
                # Flip the next three elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1  # Increment the operation count
        
        # If there are remaining 0s, return -1
        return operations if all(num == 1 for num in nums) else -1
