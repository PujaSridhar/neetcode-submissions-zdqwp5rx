# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursive call to calculate the maximum path sum for left and right child
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Current path sum includes the node itself plus the maximum gains from left and right subtrees
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain that can be extended to the parent node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum       