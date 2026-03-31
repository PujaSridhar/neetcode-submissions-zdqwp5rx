# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a stack to simulate the in-order traversal
        stack = []
        current = root
        
        while True:
            # Reach the left most Node of the current Node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            k -= 1
            # If we have found the kth smallest element
            if k == 0:
                return current.val
            
            # Otherwise, we move to the right subtree
            current = current.right        