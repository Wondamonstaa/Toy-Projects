# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        result: int = 0
        leaves = []

        def isLeaf(node) -> bool:
            return node is not None and node.left is None and node.right is None

        def dfs(node) -> int:
            
            sum: int = 0

            if node is None:
                return 0

            if isLeaf(node.left):
                leaves.append(node.left)
                sum += node.left.val
            else:
                sum += dfs(node.left)
            
            if isLeaf(node.right):
                leaves.append(node.right)
            
            sum += dfs(node.right)

            return sum
        
        result = dfs(root)
        print(leaves)
        return result
