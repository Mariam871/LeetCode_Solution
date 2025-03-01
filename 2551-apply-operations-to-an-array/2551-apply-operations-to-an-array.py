from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Apply the operations sequentially
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift non-zero elements to the left
        write = 0  # Pointer for placing non-zero elements
        
        for read in range(n):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]  # Swap non-zero with zero
                write += 1
        
        return nums

# Example usage
sol = Solution()
nums = [1, 2, 2, 1, 1, 0]
print(sol.applyOperations(nums))  # Output: [1, 4, 2, 0, 0, 0]
