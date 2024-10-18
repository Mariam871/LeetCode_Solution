class Solution:
    def countMaxOrSubsets(self, nums):
        # Step 1: Find the maximum possible OR of the entire array
        max_or = 0
        for num in nums:
            max_or |= num
        # Step 2: Count subsets with the maximum OR value
        def backtrack(index, curr_or):
            if index == len(nums):
                return 1 if curr_or == max_or else 0
            # Include the current element in the subset OR calculation
            include = backtrack(index + 1, curr_or | nums[index])
            # Exclude the current element
            exclude = backtrack(index + 1, curr_or)

            return include + exclude

        # Start backtracking from index 0 and OR value 0
        return backtrack(0, 0)
        