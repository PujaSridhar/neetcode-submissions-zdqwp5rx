class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        # Available rooms (min-heap)
        available = list(range(n))
        heapq.heapify(available)
        
        # Busy rooms: (end_time, room_number)
        busy = []
        
        # Count meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free up rooms that are done before current meeting starts
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting
                finish_time, room = heapq.heappop(busy)
                new_end = finish_time + duration
                heapq.heappush(busy, (new_end, room))
            
            count[room] += 1
        
        # Find room with max meetings (lowest index if tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i        