class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start: int) -> List[int]:
            n = len(edges)
            dist = [-1] * n
            visited = [False] * n
            queue = deque()
            queue.append((start, 0))
            visited[start] = True
            dist[start] = 0

            while queue:
                current, d = queue.popleft()
                neighbor = edges[current]
                if neighbor != -1 and not visited[neighbor]:
                    dist[neighbor] = d + 1
                    visited[neighbor] = True
                    queue.append((neighbor, d + 1))
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        minDist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                maxDist = max(dist1[i], dist2[i])
                if maxDist < minDist:
                    minDist = maxDist
                    result = i

        return result
