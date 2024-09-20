class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Reverse the string
        rev_s = s[::-1]
        
        # Check the largest palindromic prefix
        for i in range(len(s), 0, -1):
            if s[:i] == rev_s[len(s)-i:]:
                # Found the longest palindromic prefix
                break
        
        # Reverse the suffix and add it to the front
        suffix = s[i:]
        return suffix[::-1] + s
