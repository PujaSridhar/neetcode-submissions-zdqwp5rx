"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Extract start and end times from intervals
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])
        
        # Two pointers to traverse start_times and end_times
        start_pointer, end_pointer = 0, 0
        active_meetings = 0
        max_meetings = 0
        
        # Traverse through all the meetings
        while start_pointer < len(intervals):
            # If a meeting is starting before or when the previous one ends
            if start_times[start_pointer] < end_times[end_pointer]:
                active_meetings += 1
                max_meetings = max(max_meetings, active_meetings)
                start_pointer += 1
            else:
                # Meeting has ended, decrease the count of active meetings
                active_meetings -= 1
                end_pointer += 1
        
        return max_meetings
        