# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are None, then they are considered the same (empty trees)
        if not p and not q:
            return True
        # If one of the nodes is None (but not both), or if the values differ, the trees aren't the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check the left children and the right children of the current nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
