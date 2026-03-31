
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        partitions = []
        start = end = 0
        
        # Step 2: Iterate through the string and find partitions
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        
        return partitions       