import numpy as np
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        g = np.array(grid)
        n = g.shape[0]
      
        """  
        Time complexity:
        row_tuples, col_tuples, row_counter -> O(n^2) all
        sum(row_counter[col] for col in col_tuples) -> O(n^2)

        Because:
        Each row/column has n elements. There are n rows and n columns.
        Tuple creation is O(n) each -> O(n^2) total
        Counter() takes O(n) for n items -> still O(n^2)
        Final sum() iterates over n columns and does a dict lookup -> O(n)
        """
      
        row_tuples = [tuple(row) for row in g]
        col_tuples = [tuple(col) for col in g.T]
        row_counter = Counter(row_tuples)

        return sum(row_counter[col] for col in col_tuples)
