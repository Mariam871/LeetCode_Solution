class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build the graph and compute indegrees
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # DP array to store color counts for each node
        color_count = [[0] * 26 for _ in range(n)]
        queue = deque()

        # Initialize queue with nodes having 0 indegree
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            curr_color = ord(colors[node]) - ord('a')
            color_count[node][curr_color] += 1
            max_color_value = max(max_color_value, color_count[node][curr_color])

            for neighbor in graph[node]:
                # Propagate the color counts
                for c in range(26):
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c], color_count[node][c]
                    )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited == n else -1
