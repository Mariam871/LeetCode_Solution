import heapq

class Solution:
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n  # To track which elements are marked
        score = 0
        
        # Create a min-heap with elements as (value, index)
        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
        
        while min_heap:
            # Get the smallest unmarked element
            min_value, min_index = heapq.heappop(min_heap)
            
            if marked[min_index]:
                continue  # Skip if already marked
            
            # Add the value of the chosen element to the score
            score += min_value
            
            # Mark the current element and its adjacent elements
            marked[min_index] = True
            if min_index > 0:
                marked[min_index - 1] = True  # Mark the left element
            if min_index < n - 1:
                marked[min_index + 1] = True  # Mark the right element

        return score
