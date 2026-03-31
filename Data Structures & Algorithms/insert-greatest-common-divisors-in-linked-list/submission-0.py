# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            nxt = cur.next
            g = math.gcd(cur.val, nxt.val)
            
            node = ListNode(g, nxt)
            cur.next = node
            
            cur = nxt   # move to next original node
        
        return head       