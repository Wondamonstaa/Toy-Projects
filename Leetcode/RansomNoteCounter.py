from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Empty is the subset of itself
        if not ransomNote and not magazine:
            return True

        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)

        for char, count in rCounter.items():
            if mCounter[char] < count:
                return False

        return True
