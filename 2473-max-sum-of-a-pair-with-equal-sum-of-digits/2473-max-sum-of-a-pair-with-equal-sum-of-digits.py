class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = {}
        max_sum = -1

        for num in nums:
            digit_sum = sum(int(d) for d in str(num))  # Calculate digit sum
            
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, digit_sum_map[digit_sum] + num)  # Update max pair sum
            
            digit_sum_map[digit_sum] = max(digit_sum_map.get(digit_sum, 0), num)  # Store max for this digit sum
        
        return max_sum
        