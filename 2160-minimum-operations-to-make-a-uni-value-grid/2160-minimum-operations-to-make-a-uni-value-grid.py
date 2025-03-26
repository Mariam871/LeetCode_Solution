from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        elements = []
        for row in grid:
            elements.extend(row)
        
        # Check if all elements can be adjusted to a common value
        # All elements must have the same remainder when divided by x
        min_elem = min(elements)
        for num in elements:
            if (num - min_elem) % x != 0:
                return -1
        
        # Now, proceed to find the median to minimize operations
        elements.sort()
        n = len(elements)
        median = elements[n // 2]
        
        # Calculate the total operations needed to make all elements equal to the median
        operations = 0
        for num in elements:
            operations += abs(num - median) // x
        
        # For even length, the median could be elements[n//2 - 1], check both to find the minimum
        if n % 2 == 0:
            median2 = elements[n // 2 - 1]
            operations2 = 0
            for num in elements:
                operations2 += abs(num - median2) // x
            operations = min(operations, operations2)
        
        return operations