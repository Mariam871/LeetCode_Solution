class Solution:
    def minimumSteps(self, s: str) -> int:
        # Extract positions of all '1's
        positions_of_ones = [i for i, char in enumerate(s) if char == '1']

        # We need to move these '1's to consecutive positions in the array
        # Starting from some point, calculate the minimum swaps needed to group them
        total_swaps = 0

        # Target positions for the '1's should be contiguous. 
        # We can aim for the central positioning of the current `1`s
        for i, pos in enumerate(positions_of_ones):
            # Ideal position for this '1' in the grouped section
            target_pos = len(s) - len(positions_of_ones) + i
            total_swaps += abs(pos - target_pos)
        
        return total_swaps
