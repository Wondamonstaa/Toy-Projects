# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        

        result: List[int] = list()

        def dfs(node):

            if node is not None:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        result = sorted(result)
        temp: float = float('inf')

        for i in range(1, len(result)):
            temp = min(temp, abs(result[i-1] - result[i]))

        return temp
