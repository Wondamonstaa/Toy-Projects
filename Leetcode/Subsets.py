class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x = len(nums)
        return [[nums[i] for i in range(x) if j >> i & 1] for j in range(pow(2,x))]
      
