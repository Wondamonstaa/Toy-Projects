# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0  # Base case: if the root is None, tree is empty, depth is 0.
        
        # If left child is None, return min depth of right subtree + 1 (for the root)
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If right child is None, return min depth of left subtree + 1 (for the root)
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If neither child is None, return the min of the min depths of the left and right subtrees + 1 (for the root)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
