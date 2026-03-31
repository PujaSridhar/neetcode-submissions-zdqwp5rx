# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # A node is good if its value is greater than or equal to max_val
            is_good = 1 if node.val >= max_val else 0
            
            # Update the max_val for the path to the current node
            new_max_val = max(max_val, node.val)
            
            # Continue DFS traversal for left and right children
            left_good = dfs(node.left, new_max_val)
            right_good = dfs(node.right, new_max_val)
            
            return is_good + left_good + right_good
        
        # Start DFS traversal from the root with initial max_val as root's value
        return dfs(root, root.val) if root else 0        