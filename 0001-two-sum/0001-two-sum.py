class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for Left in range(len(nums)):
            for Right in range(Left + 1, len(nums)):
                if nums[Left] + nums[Right] == target:
                    return [Left, Right]
