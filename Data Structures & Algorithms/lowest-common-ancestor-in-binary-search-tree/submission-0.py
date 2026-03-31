# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Traverse the tree
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right  # LCA is in the right subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left  # LCA is in the left subtree
            else:
                return root  # This is the LCA
        return None  # In case there's no LCA (shouldn't happen in a BST with all unique values)
       