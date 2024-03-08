"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def isLeaf(node) -> bool:
            return node is not None and node.left is None and node.right is None

        if root is None:
            return 0

        if not root.children:
            return 1
        
        max_child_depth = max(self.maxDepth(child) for child in root.children)
        
        # The depth of the node is 1 (itself) plus the maximum depth among its children
        return 1 + max_child_depth

            
            
