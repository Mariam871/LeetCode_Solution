from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, curr_xor: int) -> int:
            if index == len(nums):
                return curr_xor
            # Include nums[index]
            include = dfs(index + 1, curr_xor ^ nums[index])
            # Exclude nums[index]
            exclude = dfs(index + 1, curr_xor)
            return include + exclude
        
        return dfs(0, 0)
