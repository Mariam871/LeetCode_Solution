class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
    # Create a list of (index, value) pairs, and sort it by value
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
    
        min_index = float('inf')
        max_width = 0
    
    # Iterate through the sorted indices
        for i in sorted_indices:
        # Update the maximum width where a valid ramp is found
            max_width = max(max_width, i - min_index)
        # Update the minimum index seen so far
            min_index = min(min_index, i)
    
        return max_width
