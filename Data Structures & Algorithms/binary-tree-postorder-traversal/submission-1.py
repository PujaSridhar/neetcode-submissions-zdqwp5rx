# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        lastVisited = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            peek = stack[-1]
            if peek.right and lastVisited != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                lastVisited = stack.pop()
        return result
