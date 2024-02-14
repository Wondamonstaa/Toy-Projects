class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Find the difference between the sets A and B, and B and A => put the elements in the lists
        # Wrap up the lists in a single list => return it
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
