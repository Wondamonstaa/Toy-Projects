class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        """
        Time: O(n)
        Space: O(1)
        """

        if not nums or k > len(nums):
            return 0.0

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            """
            nums = [5, 6, 1, 3, 2]
            k = 3

            # Initial window: [5, 6, 1]
            window_sum = 5 + 6 + 1 = 12

            # Slide window one step right: [6, 1, 3]
            i = 3
            nums[i] = 3
            nums[i - k] = nums[0] = 5

            window_sum += nums[i] - nums[i - k]
            window_sum += 3 - 5 → window_sum = 12 - 5 + 3 = 10
            """
            
            # window_sum = window_sum - outgoing + incoming
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        avg: float = max_sum / k

        return avg
