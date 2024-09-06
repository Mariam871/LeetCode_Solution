class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        Left = 0
        while Left < len(nums):
            if nums[Left] == val:  
                nums.pop(Left) 
            else:
                Left += 1
        return len(nums)  

