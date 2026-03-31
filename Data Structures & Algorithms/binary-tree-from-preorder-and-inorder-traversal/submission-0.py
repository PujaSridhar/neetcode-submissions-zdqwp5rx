# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The first element of preorder is the root node
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in the inorder traversal
        root_index_in_inorder = inorder.index(root_val)
        
        # Elements to the left of root_index_in_inorder are in the left subtree
        left_inorder = inorder[:root_index_in_inorder]
        # Elements to the right of root_index_in_inorder are in the right subtree
        right_inorder = inorder[root_index_in_inorder + 1:]
        
        # Corresponding elements in the preorder traversal
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root

      