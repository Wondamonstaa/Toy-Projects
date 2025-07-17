class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            
            ''' 
            [1,1,0,1]
            nums[0] == 1: zero_count = 0
            max_len = max(0, 0-0) = max(0,0) = 0

            nums[1] == 1: zero_count = 0
            max_len = max(0, 1-0) = max(0,1) = 1

            nums[2] == 0: zero_count += 1
            max_len = max(1, 2 - 0) = max(1,2) = 2

            nums[3] == 1: zero_count = 1
            max_len = max(2, 3-0) = max(2,3) = 3
            '''

            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left)

        return max_len
