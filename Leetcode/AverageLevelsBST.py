from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        if not root:
            return result
        
        queue = [root]
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for _ in range(level_count):
                current = queue.pop(0)
                level_sum += current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            # Calculate the average for the current level
            result.append(level_sum / level_count)
        
        return result
