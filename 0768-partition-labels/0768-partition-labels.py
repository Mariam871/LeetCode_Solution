class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Store the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start, end = 0, 0
        
        # Step 2: Iterate through the string and determine partitions
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Expand the partition end if needed
            
            if i == end:  # If we reached the end of a partition
                partitions.append(end - start + 1)  # Store partition size
                start = i + 1  # Move to the next partition

        return partitions
