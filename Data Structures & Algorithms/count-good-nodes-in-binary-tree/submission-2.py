# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxVal):
            if not node:
                return 0
            isGood = 1 if node.val >= maxVal else 0
            newMaxVal = max(maxVal,node.val)
            leftGood = dfs(node.left,newMaxVal)
            rightGood = dfs(node.right,newMaxVal)
            return isGood + leftGood + rightGood
        return dfs(root,root.val) if root else 0