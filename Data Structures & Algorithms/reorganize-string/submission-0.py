from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        
        # Max heap based on count (negative because heapq is min-heap)
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        
        prev_count, prev_char = 0, ''
        result = []

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            # Since we used one instance, increment count (remember negative)
            count += 1
            
            # Push the previous character back into heap if still has remaining count
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            # Set current as previous for next iteration
            prev_count, prev_char = count, char
        
        # If the result length is same as input, success
        return ''.join(result) if len(result) == len(s) else ""        