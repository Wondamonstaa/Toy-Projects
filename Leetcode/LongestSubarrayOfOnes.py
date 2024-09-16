class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if 0 not in nums:
            return len(nums) - 1

        start = end = 0
        k = 1

        for end in range(len(nums)):
            print(f"Start: {start}, end: {end}")
            if nums[end] == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
        
        return end - start 
