# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(self, root, path) -> List[int]:

            if root:
                inorder(self,root.left, path)
                path.append(root.val)
                inorder(self,root.right, path)

            return path

        path: List[int] = list()

        path = inorder(self, root, path)
        return path
