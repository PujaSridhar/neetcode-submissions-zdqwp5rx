# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        last_visited = None
        curr = root

        while curr or stack:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]

            # If right child exists and not processed yet
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                last_visited = stack.pop()

        return res       