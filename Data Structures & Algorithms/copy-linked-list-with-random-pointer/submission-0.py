"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

    # Step 1: Create new nodes and insert them right next to the original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

    # Step 2: Assign random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

    # Step 3: Restore the original list and extract the copied list
        current = head
        new_head = head.next
        while current:
            temp = current.next
            current.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            current = current.next

        return new_head      