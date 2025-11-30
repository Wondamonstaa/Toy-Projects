from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        assert grid is not None

        R, C = len(grid), len(grid[0])
        # print(f"{R} => {C}")

        def sink(r, c):

            if not ((0 <= r < R) and (0 <= c < C) and (grid[r][c] == '1')):
                return
            
            grid[r][c] = "0"

            sink(r+1, c) #down
            sink(r-1, c) #up
            sink(r, c-1) #left
            sink(r, c+1) #right

        return sum(
            grid[r][c] == '1' and (sink(r,c) or True)
            for r in range(R)
            for c in range(C)
        )
        
