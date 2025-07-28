class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        if not nums1:
            return [nums2]
        if not nums2: 
            return [nums1]

        s1, s2 = set(nums1), set(nums2)

        r1 = list(s1.difference(s2))
        r2 = list(s2.difference(s1))
        r = [r1, r2]

        return r
