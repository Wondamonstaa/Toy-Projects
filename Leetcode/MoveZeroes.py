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
