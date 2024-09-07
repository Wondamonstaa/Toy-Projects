from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Add all initial rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If no fresh oranges are present, return 0
        if fresh_count == 0:
            return 0
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        minutes = 0
        
        # BFS to spread rot
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            
            # Increment minutes after processing all rotten oranges in the current minute
            minutes += 1
        
        # If there are still fresh oranges left, return -1
        return minutes - 1 if fresh_count == 0 else -1
