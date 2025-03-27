class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element
        freq = Counter(nums)
        n = len(nums)
        
        # Find the element with the highest frequency
        dominant = max(freq, key=freq.get)
        total_count = freq[dominant]
        
        # Step 2: Find the minimum index where we can split
        count_left = 0
        
        for i in range(n - 1):
            if nums[i] == dominant:
                count_left += 1
            
            count_right = total_count - count_left  # Remaining count in the right subarray
            
            if count_left * 2 > (i + 1) and count_right * 2 > (n - i - 1):
                return i
        
        return -1  # No valid split found
