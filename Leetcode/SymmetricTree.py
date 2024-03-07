# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        # Check if the current nodes are equal and
        # if the left child of the left node equals the right child of the right node,
        # and if the right child of the left node equals the left child of the right node.
        return (left.val == right.val and 
                self.isMirror(left.right, right.left) and 
                self.isMirror(left.left, right.right))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
