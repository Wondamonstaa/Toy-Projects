class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lnzi = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lnzi] = nums[i]
                lnzi += 1
        
        for i in range(lnzi, len(nums)):
            nums[i] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z] = nums[i]
                z += 1
                
        for i in range(z, len(nums)):
            nums[i] = 0


# Second

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0 
        c = 0
        
        for num in nums:
            if num != 0:
                nums[start] = num
                start += 1

        while start < len(nums):
            nums[start] = 0
            start += 1
