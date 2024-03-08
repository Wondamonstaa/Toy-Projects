class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Hash set
        h = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in h:
                return [h[complement], i]

            h[num] = i
