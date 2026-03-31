class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for i in s:
            if i in dictS:
                dictS[i] += 1
            else:
                dictS[i] = 1
        for i in t:
            if i in dictT:
                dictT[i] += 1
            else:
                dictT[i] = 1
        return dictS == dictT