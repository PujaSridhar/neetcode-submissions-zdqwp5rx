class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4
        for i in range(n-1,-1,-1):
            res = stoneValue[i] - dp[(i+1)%4]
            if i + 1 < n:
                res = max(res,stoneValue[i] + stoneValue[i+1] - dp[(i+2)%4])
            if i + 2 < n:
                res = max(res,stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[(i+3)%4])
            dp[i%4] = res
        alice = dp[0]
        if alice > 0 : return 'Alice'
        if alice < 0: return 'Bob'
        return 'Tie'