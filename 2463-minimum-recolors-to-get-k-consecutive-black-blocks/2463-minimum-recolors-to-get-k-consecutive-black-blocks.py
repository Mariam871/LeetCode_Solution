class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count the number of 'W' in the first window of size k
        min_operations = blocks[:k].count('W')
        current_operations = min_operations

        # Slide the window across the string
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':  # Remove the leftmost element from the window
                current_operations -= 1
            if blocks[i] == 'W':  # Add the new element to the window
                current_operations += 1
            
            min_operations = min(min_operations, current_operations)

        return min_operations
