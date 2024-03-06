class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        # Helper function to reverse elements in place
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        # Step 1: Reverse the entire list
        reverse(0, n-1)
        # Step 2: Reverse the first k elements
        reverse(0, k-1)
        # Step 3: Reverse the rest
        reverse(k, n-1)

        
