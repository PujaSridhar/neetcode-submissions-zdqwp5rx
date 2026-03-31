# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
    
        while curr is not None:
            next_node = curr.next  # Store next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev one step forward
            curr = next_node       # Move curr one step forward
    
        return prev  # prev will be the new head after the loop ends      