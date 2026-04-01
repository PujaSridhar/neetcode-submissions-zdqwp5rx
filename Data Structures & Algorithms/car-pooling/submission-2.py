class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for numPassengers, start, end in trips:
            events.append((start, numPassengers))
            events.append((end, -numPassengers))
        
        events.sort()

        currPassenger = 0
        for loc, change in events:
            currPassenger += change
            if currPassenger > capacity:
                return False
        return True