class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: convert to lowercase
        s = s.lower()
        # Remove all non-alphanumeric characters
        s = re.sub(r'[^a-z0-9]', '', s)
        # Check if the string reads the same forwards and backwards
        return s == s[::-1]
        