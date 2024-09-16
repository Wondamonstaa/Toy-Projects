class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = end = 0

        for end in range(len(nums)):
            print(f"Current nums[end]: {nums[end]}")
            if nums[end] == 0:
                print(f"Start: {start}, end: {end}")
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

        return end - start + 1
