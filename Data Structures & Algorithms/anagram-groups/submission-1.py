from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                arr[pos] += 1
            
            anagrams[tuple(arr)].append(s)
        
        result = []
        for k, v in anagrams.items():
            result.append(v)
        
        return result

