import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert the gifts list into a max-heap by negating the elements
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        # Perform the operation k times
        for _ in range(k):
            # Get the largest pile (smallest in negative form)
            max_gifts = -heapq.heappop(max_heap)
            # Calculate the remaining gifts after taking the square root
            remaining_gifts = math.floor(math.sqrt(max_gifts))
            # Push the remaining gifts back into the heap (as negative)
            heapq.heappush(max_heap, -remaining_gifts)
        
        # Calculate the total remaining gifts
        return -sum(max_heap)
