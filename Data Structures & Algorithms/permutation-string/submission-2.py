class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        def can_create(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return count
        s1_count = can_create(s1)
        window_count = can_create(s2[:len(s1)])
        if s1_count == window_count:
            return True
        for i in range(len(s1),len(s2)):
            new_char = s2[i]
            old_char = s2[i-len(s1)]
            window_count[ord(new_char) - ord('a')] += 1
            window_count[ord(old_char) - ord('a')] -= 1
            if s1_count == window_count:
                return True
        return False   