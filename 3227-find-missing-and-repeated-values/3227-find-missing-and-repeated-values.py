class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n  # Total expected numbers from 1 to n^2

        expected_sum = N * (N + 1) // 2
        expected_sum_sq = (N * (N + 1) * (2 * N + 1)) // 6

        actual_sum = actual_sum_sq = 0
        num_count = {}

        # Iterate through the grid
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sum_sq += num * num
                num_count[num] = num_count.get(num, 0) + 1

        # Find the repeating number (a)
        for num, count in num_count.items():
            if count == 2:
                a = num
                break

        # Solve for the missing number (b)
        b = expected_sum - (actual_sum - a)

        return [a, b]
