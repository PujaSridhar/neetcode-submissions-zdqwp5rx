class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != '#':
                j += 1
            # Get the length of the next string
            length = int(s[i:j])
            # Move i to the start of the actual string
            i = j + 1
            # Extract the string
            decoded.append(s[i:i+length])
            # Move i to the start of the next length substring
            i += length
        return decoded