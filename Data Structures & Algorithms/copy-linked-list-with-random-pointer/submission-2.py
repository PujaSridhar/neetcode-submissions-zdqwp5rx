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
            return
        current = head
        while current:
            newNode = Node(current.val)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        newHead = head.next
        while current:
            tmp = current.next
            current.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            current = current.next
        return newHead
