class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        cur = 0
        result = []

        i, j = 0, len(numbers) - 1

        while i < j:

            cur = numbers[i] + numbers[j]

            if cur  == target:
                return [i + 1, j + 1]
            elif cur < target:
                i += 1
            else:
                j -= 1
            
        return []
