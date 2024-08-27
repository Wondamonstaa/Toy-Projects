class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []

        l1, l2 = len(word1), len(word2)

        for i in range(max(l1, l2)):
            if i < l1:
                merged.append(word1[i])
            if i < l2:
                merged.append(word2[i])

        return ''.join(merged)
