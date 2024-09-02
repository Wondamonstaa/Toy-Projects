from functools import reduce 
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        a = 0
        n = 1
        result = nums.copy()
        zero_count = nums.count(0)
        overall_product = reduce(operator.mul, nums, 1)

        '''
        1,2,3,4
        prefix = [1]
        suffix = [2,3,4]
        current = 2*3*4 => replace 1 => 1 becomes 24
        list = [24, 2, 3, 4] => move to the next digit
        '''

        if zero_count > 1:
            return [0] * len(nums)

        """for i in range(len(nums)):
            current = nums[i]
            prefix = nums[a:n]
            suffix = nums[n:]
            elements = [char for idx, char in enumerate(nums) if idx != i]
            print(f"Elements: {elements}")
            r = reduce(operator.mul, elements, 1)
            current = r
            result[i] = current
            n += 1
            '''print(
                f"New prefix: {prefix},", 
                f"current element: {nums[i]},",
                f"new suffix: {suffix}")'''"""
        
        for i in range(len(nums)):
            if nums[i] == 0:
                # Special case: when there's exactly one zero in the array
                result[i] = reduce(
                    operator.mul, 
                    [nums[j] for j in range(len(nums)) if j != i], 1)
            else:
                '''
                [1,2,3,4]
                overall_product = 1*2*3*4 = 24
                i = 1
                result[1] = 24 // 1 = 24
                i = 2
                result[2] = 24 // 2 = 12
                i = 3
                result[3] = 24 // 3 = 8
                i = 4
                result[4] = 24 // 4 = 6
                result = [24, 12, 8, 6]
                '''
                result[i] = overall_product // nums[i]

        return result
