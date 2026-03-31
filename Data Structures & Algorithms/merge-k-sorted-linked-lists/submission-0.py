import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Add comparison operator so heapq can sort ListNode objects by val
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Initialize the heap with the head of each non-empty list
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        dummy = ListNode()
        current = dummy

        while heap:
            # Pop the smallest node from the heap
            node = heapq.heappop(heap)
            current.next = node
            current = current.next

            # If the node has a next, push it into the heap
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next