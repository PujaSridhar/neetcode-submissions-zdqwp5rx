class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            res = []
            for end in range(start+1,len(s)+1):
                word = s[start:end]
                if word in wordSet:
                    subs = dfs(end)
                    for sub in subs:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)
            memo[start] = res
            return res
        return dfs(0)