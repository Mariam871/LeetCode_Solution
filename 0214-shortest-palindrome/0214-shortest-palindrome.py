class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        rev_s = s[::-1]
        for i in range(len(s), 0, -1):
            if s[:i] == rev_s[len(s)-i:]:
                break
        suffix = s[i:]
        return suffix[::-1] + s
