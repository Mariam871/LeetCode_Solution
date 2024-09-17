class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left=0
        for k in range(1, len(nums)):
            if nums[k] != nums[left]:
                left+=1
                nums[left] = nums[k]
        return left + 1