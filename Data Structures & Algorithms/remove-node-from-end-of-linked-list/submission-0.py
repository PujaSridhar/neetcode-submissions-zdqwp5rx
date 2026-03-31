# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
    
    # Step 1: Advance first pointer by n+1 steps
        for _ in range(n + 1):
            first = first.next
    
    # Step 2: Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
    
    # Step 3: Skip the nth node
        second.next = second.next.next
    
    # Return the head of the modified list
        return dummy.next       