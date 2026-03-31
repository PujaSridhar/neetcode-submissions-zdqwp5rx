class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        def canCreate(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return count
        
        s1Count = canCreate(s1)
        windowCount = canCreate(s2[:len(s1)])
        if s1Count == windowCount:
            return True

        for i in range(len(s1), len(s2)):
            newChar = s2[i]
            oldChar = s2[i-len(s1)]
            windowCount[ord(newChar) - ord('a')] += 1
            windowCount[ord(oldChar) - ord('a')] -= 1
            if s1Count == windowCount:
                return True
        return False