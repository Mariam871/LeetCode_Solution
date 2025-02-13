class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heappop(nums)  # Smallest element
            y = heappop(nums)  # Second smallest element
            new_val = (min(x, y) * 2) + max(x, y)  # Merge formula
            heappush(nums, new_val)  # Push back the new element
            operations += 1  # Increment operation count

        return operations

        