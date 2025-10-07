class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1 
        
        from collections import defaultdict
        
        m = defaultdict(list)
        window = len(needle)
        
        # Slide window by 1
        for i in range(len(haystack) - window + 1):
            piece = haystack[i:i+window]
            m[piece].append(i)
        
        if needle in m:
            return min(m[needle])
        else:
            return -1
