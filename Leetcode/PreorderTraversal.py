# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        path: List[int] = list()

        def preorder(self, root, param):

            if root:
                param.append(root.val)
                param = preorder(self, root.left, param)
                param = preorder(self, root.right, param)

            return param

        path = preorder(self, root, path)

        return path
            
