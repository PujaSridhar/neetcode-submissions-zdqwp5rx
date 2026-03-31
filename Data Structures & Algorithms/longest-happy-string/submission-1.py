import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max heap with negative counts (because heapq is min heap in Python)
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []

        while heap:
            count1, char1 = heapq.heappop(heap)
            # If last two letters are the same as char1, pick next most frequent
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  # no alternative, stop
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1  # decrement usage (negative numbers)
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count1, char1))  # push back
            else:
                result.append(char1)
                count1 += 1  # decrement usage
                if count1 != 0:
                    heapq.heappush(heap, (count1, char1))

        return ''.join(result)        