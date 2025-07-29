from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        c1, c2 = Counter(word1), Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        return Counter(c1.values()) == Counter(c2.values())
