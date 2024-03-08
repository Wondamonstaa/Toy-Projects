class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, currentPath, currentSum):
            if not node:
                return
            # Include the current node's value in the path
            currentPath.append(node.val)
            currentSum += node.val
            # Check if it's a leaf node and the path sum equals targetSum
            if not node.left and not node.right and currentSum == targetSum:
                # Make a deep copy of the currentPath since we will backtrack
                result.append(list(currentPath))
            else:
                # Continue to search the path in the left and right subtree
                dfs(node.left, currentPath, currentSum)
                dfs(node.right, currentPath, currentSum)
            # Backtrack: remove the current node before going up the recursive call stack
            currentPath.pop()
        
        result = []
        dfs(root, [], 0)
        return result
