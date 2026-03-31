class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time, and by end time if start times are the same
        intervals.sort()
        
        # Pair each query with its original index and sort the queries
        queries_with_indices = sorted([(q, i) for i, q in enumerate(queries)])
        
        # Min-heap to keep track of the intervals based on their length
        min_heap = []
        result = [-1] * len(queries)
        interval_index = 0
        
        # Process each query
        for query, original_index in queries_with_indices:
            # Add all intervals that start before or when the query point occurs
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                left, right = intervals[interval_index]
                heapq.heappush(min_heap, (right - left + 1, right))
                interval_index += 1
            
            # Remove all intervals that end before the query point
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # The smallest valid interval is now on top of the heap
            if min_heap:
                result[original_index] = min_heap[0][0]
        
        return result        