# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def longestPath(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the longest path in both left child and right child
            left_path = longestPath(node.left)
            right_path = longestPath(node.right)
            
            # Path that passes through the node will be the sum of longest path in left child and right child
            self.diameter = max(self.diameter, left_path + right_path)
            
            # Return the longest one between left_path and right_path; add 1 for the current node
            return max(left_path, right_path) + 1
        
        longestPath(root)
        return self.diameter
        