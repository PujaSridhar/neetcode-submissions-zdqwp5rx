# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def longestpath(node:Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_path = longestpath(node.left)
            right_path = longestpath(node.right)
            self.diameter = max(self.diameter,left_path + right_path)
            return max(left_path,right_path) + 1
        longestpath(root)
        return self.diameter