# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, low: float, high: float) -> bool:
            if not node:
                return True
            
            # Check if the current node's value is within the valid range
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively validate the left and right subtrees with updated ranges
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Initialize the validation with the whole range of valid values
        return validate(root, float('-inf'), float('inf'))        