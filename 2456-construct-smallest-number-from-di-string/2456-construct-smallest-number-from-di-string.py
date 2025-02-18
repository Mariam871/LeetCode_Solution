class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        
        for i in range(len(pattern) + 1):  # Loop through pattern + 1 times
            stack.append(str(i + 1))  # Push current number
            
            if i == len(pattern) or pattern[i] == 'I':  # When 'I' is encountered or at end
                while stack:
                    result.append(stack.pop())  # Pop from stack in LIFO order
        
        return ''.join(result)  # Return final result after the loop completes
