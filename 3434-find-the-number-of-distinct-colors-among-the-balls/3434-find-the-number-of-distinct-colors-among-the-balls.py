class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Maps each ball to its current color
        color_count = defaultdict(int)  # Counts occurrences of each color
        distinct_colors = set()  # Keeps track of distinct colors
        result = []

        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    distinct_colors.discard(old_color)
            
            # Assign new color
            ball_colors[x] = y
            color_count[y] += 1
            distinct_colors.add(y)

            # Append the current count of distinct colors
            result.append(len(distinct_colors))

        return result

        