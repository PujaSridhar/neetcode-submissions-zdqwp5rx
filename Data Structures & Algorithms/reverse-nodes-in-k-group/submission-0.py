class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper: Check if at least k nodes remain
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        # Helper: Reverse k nodes starting at node
        def reverse_k_nodes(start, k):
            prev = None
            curr = start
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, start, curr  # new head, new tail, next group's start

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        curr = head

        while has_k_nodes(curr, k):
            new_head, new_tail, next_group_start = reverse_k_nodes(curr, k)
            group_prev.next = new_head
            new_tail.next = next_group_start
            group_prev = new_tail
            curr = next_group_start

        return dummy.next
