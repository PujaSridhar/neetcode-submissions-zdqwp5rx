class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        window = 0  # number of reachable positions in sliding window

        for i in range(1, n):
            # add new left boundary
            if i - minJump >= 0 and dp[i - minJump]:
                window += 1

            # remove out-of-range right boundary
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                window -= 1

            # reachable if window > 0 and current is '0'
            if window > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]        