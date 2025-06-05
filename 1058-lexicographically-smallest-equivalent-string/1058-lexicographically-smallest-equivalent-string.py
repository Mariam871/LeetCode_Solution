class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union-Find structure to track character equivalences
        parent = [i for i in range(26)]  # for 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            # Always keep the lexicographically smaller character as parent
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Build equivalence classes
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        # Build the result using smallest equivalent characters
        result = []
        for c in baseStr:
            smallest = find(ord(c) - ord('a'))
            result.append(chr(smallest + ord('a')))

        return ''.join(result)
