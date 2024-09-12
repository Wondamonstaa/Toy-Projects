class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        current_sum = sum(nums[:k])
        print(f"First window's sum: {current_sum}")
        max_sum = current_sum
       
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        average = max_sum / k
        
        return average
