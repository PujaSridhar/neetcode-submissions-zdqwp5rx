class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(s))
            map[sortedStr].append(s)
        return list(map.values())