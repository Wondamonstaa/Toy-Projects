class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while n > 0:
            nums1.pop()
            n -= 1

        nums1.extend(nums2)
        nums1.sort()

#OR
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums3 = [x for x in nums1[:m]]
        
        nums3.extend(nums2)
        
        nums3.sort()
        
        for i in range(len(nums3)):
            nums1[i] = nums3[i]
        
