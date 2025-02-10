class Solution:
    def clearDigits(self, s: str) -> str:  # Rename method to match the expected function name
        stack = []
    
        for char in s:
            if char.isdigit():
                if stack:  
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

# Test case
sol = Solution()
print(sol.clearDigits("a1b2c3"))  # Output: ""
