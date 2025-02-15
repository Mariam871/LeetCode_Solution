class Solution:
    def canPartition(self, s: str, target: int, index: int, current_sum: int) -> bool:
        """
        Backtracking function to check if we can partition the squared number
        into contiguous substrings that sum up to 'target'.
        """
        if index == len(s):
            return current_sum == target
        
        num = 0
        for j in range(index, len(s)):
            num = num * 10 + int(s[j])  # Form number from substring
            if current_sum + num > target:
                break  # Stop early if sum exceeds target
            if self.canPartition(s, target, j + 1, current_sum + num):
                return True
        
        return False

    def punishmentNumber(self, n: int) -> int:
        total_punishment = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if self.canPartition(square_str, i, 0, 0):
                total_punishment += i * i
        return total_punishment

# Example usage:
sol = Solution()
print(sol.punishmentNumber(10))  # Output: 182

        