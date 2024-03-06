class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curVal):
            if not node:
                return 0
            
            curVal = curVal * 10 + node.val  # Accumulate the current path value
            
            # If it's a leaf node, return the current path value
            if not node.left and not node.right:
                return curVal
            
            # Recursively sum the values from left and right subtrees
            leftSum = dfs(node.left, curVal)
            rightSum = dfs(node.right, curVal)
            
            return leftSum + rightSum

        return dfs(root, 0)
