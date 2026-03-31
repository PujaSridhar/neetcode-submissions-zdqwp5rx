"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to save the cloned nodes
        cloned_nodes = {}

        # Helper function to perform DFS
        def dfs(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Clone the node
            clone = Node(node.val)
            cloned_nodes[node] = clone
            
            # Clone all the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)        