import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        num_queries = len(queries)
        result = [0] * num_queries
        
        # Create a list of queries with their original indices for sorting
        sorted_queries = sorted((val, idx) for idx, val in enumerate(queries))
        
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for query_val, query_idx in sorted_queries:
            while min_heap and min_heap[0][0] < query_val:
                val, i, j = heapq.heappop(min_heap)
                count += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(min_heap, (grid[ni][nj], ni, nj))
            result[query_idx] = count
        
        return result