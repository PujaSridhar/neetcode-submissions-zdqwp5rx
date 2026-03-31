class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDeg = [0] * (n + 1)
        outDeg = [0] * (n + 1)

        for a, b in trust:
            outDeg[a] += 1
            inDeg[b] += 1

        for i in range(1, n + 1):
            if inDeg[i] == n - 1 and outDeg[i] == 0:
                return i

        return -1        