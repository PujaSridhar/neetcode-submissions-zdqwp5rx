# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy
    
    # Initialize pointers for both lists
        l1, l2 = list1, list2
    
    # Traverse both lists and append the smaller node to the new list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
    
    # Attach the remaining nodes of l1 or l2, if any
        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
    
    # Return the merged list, starting from the node after dummy
        return dummy.next
