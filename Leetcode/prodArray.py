import numpy as np
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
          return []
          
        n = len(nums)
        arr = np.array(nums)

        # Left cumulative product, shifting right by 1 and inserting 1 at the start
        left = np.empty(n, dtype=int)
        left[0] = 1
        left[1:] = np.cumprod(arr[:-1])

        # Right cumulative product, shifting left by 1 and inserting 1 at the end
        right = np.empty(n, dtype=int)
        right[-1] = 1
        right[:-1] = np.cumprod(arr[::-1][:-1])[::-1]
      
        result = left * right
        return result.tolist()
