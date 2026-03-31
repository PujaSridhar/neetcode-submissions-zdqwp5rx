class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

    # Function to create a character count array
        def create_char_count(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return count

        s1_count = create_char_count(s1)
        window_count = create_char_count(s2[:len(s1)])

    # Check the initial window
        if s1_count == window_count:
            return True

    # Slide the window over s2
        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            old_char = s2[i - len(s1)]
        
        # Update the window counts
            window_count[ord(new_char) - ord('a')] += 1
            window_count[ord(old_char) - ord('a')] -= 1

        # Check if current window matches s1 count
            if s1_count == window_count:
                return True

        return False       