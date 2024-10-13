class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # Set to keep track of elements in the current window
        
        for i in range(len(nums)):
            # If the index exceeds k, remove the element that is out of the window
            if i > k:
                seen.remove(nums[i - k - 1])  # Remove the element that is k indices behind
            
            # Check if the current number is already in the set
            if nums[i] in seen:
                return True  # Found a duplicate within range k
            
            # Add the current number to the set
            seen.add(nums[i])
        
        return False  # No duplicates found within range k