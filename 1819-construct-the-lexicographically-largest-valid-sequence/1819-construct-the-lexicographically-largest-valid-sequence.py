class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1  # The total length of the sequence
        res = [0] * size  # Initialize the sequence with 0s
        used = set()  # Track used numbers

        def backtrack(index):
            # If we have filled the sequence, return True
            if index == size:
                return True

            # If the current position is already filled, move to the next
            if res[index] != 0:
                return backtrack(index + 1)

            # Try placing the numbers from n down to 1
            for num in range(n, 0, -1):
                if num in used:
                    continue  # Skip already used numbers

                if num == 1:  # 1 occurs only once
                    res[index] = num
                    used.add(num)
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used.remove(num)
                else:
                    # Check if both placements (index and index + num) are valid
                    if index + num < size and res[index] == 0 and res[index + num] == 0:
                        res[index] = res[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        # Backtrack
                        res[index] = res[index + num] = 0
                        used.remove(num)

            return False  # No valid placement found

        backtrack(0)
        return res