class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')  # Initialize to infinity

        def inorder(node):
            nonlocal prev, min_diff
            if node is not None:
                inorder(node.left)
                if prev is not None:
                    min_diff = min(min_diff, node.val - prev.val)
                prev = node 
                inorder(node.right)
        
        inorder(root)
        return min_diff
