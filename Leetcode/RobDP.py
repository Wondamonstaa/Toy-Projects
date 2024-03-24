class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob_prev_prev = nums[0]  # Max robbed amount up to two houses back
        rob_prev = max(nums[0], nums[1])  # Max robbed amount up to the previous house
        
        for i in range(2, len(nums)):
            current = max(rob_prev, rob_prev_prev + nums[i])
            rob_prev_prev, rob_prev = rob_prev, current
        
        return rob_prev
