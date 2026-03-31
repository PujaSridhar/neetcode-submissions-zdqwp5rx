class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged list is empty or there's no overlap, add the interval to merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap detected, merge the current interval with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged        