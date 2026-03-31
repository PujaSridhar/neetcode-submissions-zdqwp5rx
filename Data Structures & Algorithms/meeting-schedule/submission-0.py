"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort intervals by their start time
        intervals.sort(key=lambda x: x.start)
        
        # Step 2: Check for overlaps between consecutive intervals
        for i in range(1, len(intervals)):
            # If the current interval's end time is greater than the next interval's start time, return False
            if intervals[i-1].end > intervals[i].start:
                return False
        
        # Step 3: If no overlaps are found, return True
        return True