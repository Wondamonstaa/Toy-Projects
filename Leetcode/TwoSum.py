class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize the hash table
        h = {}

        # Enumerate

        for i, num in enumerate(nums):

            # Complement
            complement = target - num
            
            # Check if complement in a hash table already
            if complement in h:
                return [h[complement], i]


            h[num] = i
