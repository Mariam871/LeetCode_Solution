from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build graph as adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Step 2: Dijkstra's initialization
        dist = [float('inf')] * n  # Shortest time to reach each node
        ways = [0] * n  # Ways to reach each node in shortest time
        dist[0] = 0
        ways[0] = 1

        # Min-heap to process nodes (time, node)
        pq = [(0, 0)]  # (travel time, node)

        while pq:
            time, node = heappop(pq)

            # If already processed with shorter time, skip
            if time > dist[node]:
                continue

            # Process neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time
                
                # If a shorter path is found
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(pq, (new_time, neighbor))
                
                # If another shortest path is found
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
