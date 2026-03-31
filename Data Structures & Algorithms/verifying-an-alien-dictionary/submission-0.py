class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            mismatch = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    mismatch = True
                    break

            # prefix case: "neetcode" before "neet"
            if not mismatch and len(w1) > len(w2):
                return False

        return True        