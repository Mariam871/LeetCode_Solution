class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        digit_sum_groups = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            digit_sum_groups[digit_sum] += 1

        max_size = max(digit_sum_groups.values())
        return sum(1 for size in digit_sum_groups.values() if size == max_size)
