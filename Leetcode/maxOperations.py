from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # freq = Counter(nums)
        count = 0

        # for num in nums:
        #     if freq[num] == 0:
        #         continue

        #     complement = k - num
        #     if freq[complement] > 0:
        #         if num == complement and freq[num] < 2:
        #             continue  # NOTE: need at least two of the same number
        #         freq[num] -= 1
        #         freq[complement] -= 1
        #         count += 1

        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return count
