class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for numPassengers, start, end in trips:
            events.append((start, numPassengers))  # pick up
            events.append((end, -numPassengers))   # drop off

        # Sort events by location
        events.sort()

        curr_passengers = 0
        for loc, change in events:
            curr_passengers += change
            if curr_passengers > capacity:
                return False

        return True        