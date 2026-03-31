# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
    
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
        
        # Create new node with the computed value
            current.next = ListNode(new_val)
            current = current.next
        
        # Move to the next nodes in l1 and l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
    
        return dummy_head.next
        