class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookup.
        word_set = set(wordDict)
        
        # Create a dp array of size len(s) + 1 and initialize all to False.
        dp = [False] * (len(s) + 1)
        
        # Base case: an empty string can be segmented.
        dp[0] = True
        
        # Fill the dp array.
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        # The result is whether the entire string can be segmented.
        return dp[len(s)]        