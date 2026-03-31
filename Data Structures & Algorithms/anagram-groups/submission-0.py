class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        return list(anagram_map.values())