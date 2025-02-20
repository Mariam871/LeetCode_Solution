class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        # Create a binary string by flipping the diagonal elements
        result = ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
        return result
        