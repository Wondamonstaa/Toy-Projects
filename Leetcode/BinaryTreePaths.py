class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths: List[str] = list()

        def dfs(node: Optional[TreeNode], path: str, paths: List[str]) -> None:

            if node:
                
                # Obtain a value => add to the string
                newPath = path + str(node.val)

                # No more leaves
                if not node.left and not node.right:
                    
                    # New path discovered
                    paths.append(newPath)

                else:

                    dfs(node.left, newPath + "->", paths)
                    dfs(node.right, newPath + "->", paths)

        dfs(root, "", paths)

        return paths





