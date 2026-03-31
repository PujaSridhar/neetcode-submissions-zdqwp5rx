class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        
        # Add original index to tasks
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()  # sort by enqueueTime
        
        result = []
        minHeap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or minHeap:
            
            # If no available tasks, jump time forward
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]
            
            # Push all available tasks into heap
            while i < n and tasks[i][0] <= time:
                _, pt, idx = tasks[i]
                heapq.heappush(minHeap, (pt, idx))
                i += 1
            
            # Process next task
            pt, idx = heapq.heappop(minHeap)
            time += pt
            result.append(idx)
        
        return result        