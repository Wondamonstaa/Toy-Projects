from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build a frequency map
        frequency_map = Counter(nums)
        
        # Step 2: Sort the elements by frequency in descending order and get the top k elements
        top_k = [element for element, frequency in frequency_map.most_common(k)]
        
        return top_k
