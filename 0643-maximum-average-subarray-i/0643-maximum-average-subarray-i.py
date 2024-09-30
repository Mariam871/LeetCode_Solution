class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Calculate the sum of the first k elements (first window)
     current_sum = sum(nums[:k])
     max_sum = current_sum
    
    # Slide the window from index k to the end of the array
     for i in range(k, len(nums)):
        # Slide the window: subtract the element going out and add the new element
        current_sum = current_sum - nums[i - k] + nums[i]
        # Track the maximum sum
        max_sum = max(max_sum, current_sum)
    
    # Return the maximum average
     return max_sum / k