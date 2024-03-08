class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if not nums:
            return False
        
        # Use a hash set to store elements in the current window of size k
        seen = set()
        
        for i, num in enumerate(nums):
            # If num is already in the set, we found a nearby duplicate
            if num in seen:
                return True
            
            # Add the current num to the set
            seen.add(num)
            
            # Ensure the window size does not exceed k
            # When the window size exceeds k, remove the oldest element from the set
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False
