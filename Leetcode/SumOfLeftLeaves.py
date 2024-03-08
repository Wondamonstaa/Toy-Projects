# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        def dfs(node) -> int:
            
            sum: int = 0

            if node is None:
                return 0

            if isLeaf(node.left):
                sum += node.left.val
            else:
                sum += dfs(node.left)

            sum += dfs(node.right)

            return sum

        sum: int = 0

        sum = dfs(root)

        return sum

