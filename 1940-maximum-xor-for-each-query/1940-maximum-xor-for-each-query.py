from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the maximum possible value for k
        max_val = (1 << maximumBit) - 1  # This is 2^maximumBit - 1
        
        # Calculate the initial XOR of all elements in nums
        current_xor = 0
        for num in nums:
            current_xor ^= num
        
        # Prepare the answer list
        answer = []
        
        # Process each query from the end of nums to the beginning
        for num in reversed(nums):
            # Calculate k as the XOR of current_xor and max_val
            k = current_xor ^ max_val
            answer.append(k)
            
            # Update the current XOR by removing the last element in nums
            current_xor ^= num
        
        return answer


        