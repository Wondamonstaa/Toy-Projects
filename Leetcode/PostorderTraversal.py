# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        path: List[int] = list()

        def postorder(self, root: Optional[TreeNode], path: List[int]) -> List[int]:

            if root:

                postorder(self, root.left, path)
                postorder(self, root.right, path)
                path.append(root.val)

            return path

        path = postorder(self, root, path)

        return path
