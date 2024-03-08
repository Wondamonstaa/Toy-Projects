class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in strs
        shortest = min(strs)
        
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    # Return the common prefix up to the point of mismatch
                    return shortest[:i]
        
        return shortest
