class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # i = 0

        # while k > 0:
            
        #     tail = nums.pop()
        #     nums.reverse()
        #     nums.append(tail)
        #     nums.reverse()

        #     k -= 1

        n = len(nums)
        if n == 0:
            return
        k %= n 
        print(k)
        nums[:] = nums[-k:] + nums[:-k]

        
