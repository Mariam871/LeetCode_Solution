class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
        cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string is equal to its reverse
        return cleaned_str == cleaned_str[::-1]
        