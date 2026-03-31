class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Step 1: Sort the intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize count of removals and set the end time of the first interval
        count = 0
        prev_end = intervals[0][1]
        
        # Step 2: Iterate through the intervals and count overlaps
        for i in range(1, len(intervals)):
            # If the current interval starts before the previous interval ends, there's an overlap
            if intervals[i][0] < prev_end:
                count += 1
            else:
                # No overlap, update the end time to the current interval's end
                prev_end = intervals[i][1]
        
        return count        