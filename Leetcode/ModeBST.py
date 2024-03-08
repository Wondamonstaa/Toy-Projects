class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Dictionary to count occurrences of each value
        count = {}
        
        # Helper function to perform in-order traversal and count values
        def inorder(node):
            if node:
                inorder(node.left)
                count[node.val] = count.get(node.val, 0) + 1
                inorder(node.right)
                
        inorder(root)
        
        # Find the maximum occurrence(s)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]
