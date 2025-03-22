from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # Step 2: DFS to find connected components
        visited = set()
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)  # Visit unvisited neighbors

        complete_count = 0
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)
                
                # Step 3: Check if component is complete
                k = len(component)
                total_edges = sum(len(graph[v]) for v in component) // 2
                if total_edges == k * (k - 1) // 2:
                    complete_count += 1
        
        return complete_count
