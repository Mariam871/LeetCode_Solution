class Solution:
        def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
            count = 0
            allowed_set = set(allowed)          
            for word in words:
                if all(c in allowed_set for c in word):
                    count += 1
            return count
