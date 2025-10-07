class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        assert all(v is not None for v in [nums, val])
        k = 0

        # Two pointer approach
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
