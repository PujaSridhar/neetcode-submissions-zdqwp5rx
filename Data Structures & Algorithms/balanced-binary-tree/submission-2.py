# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node:Optional[TreeNode]) ->Tuple[bool,int]:
            if not node:
                return True, 0
            leftBalanced, leftHeight = height(node.left)
            rightBalanced, rightHeight = height(node.right)
            isBalanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
            currentHeight = max(leftHeight, rightHeight) + 1
            return isBalanced, currentHeight
        balanced, _ = height(root)
        return balanced