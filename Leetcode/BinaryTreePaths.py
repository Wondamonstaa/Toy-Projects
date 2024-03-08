class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, path, paths):
            if node:
                newPath = path + str(node.val)
                # If it's a leaf node, append the path to the list of paths
                if not node.left and not node.right:
                    paths.append(newPath)
                else:
                    # Continue the depth-first search on both children
                    dfs(node.left, newPath + "->", paths)
                    dfs(node.right, newPath + "->", paths)
        
        paths = []
        dfs(root, "", paths)

        return paths
