class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            if "".join(stack[-part_len:]) == part:  # Check if the last characters match `part`
                del stack[-part_len:]  # Remove `part` from the stack

        return "".join(stack)

