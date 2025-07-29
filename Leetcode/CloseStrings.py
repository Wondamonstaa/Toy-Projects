from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Check if the frequencies of characters in both words can be sorted
        return sorted(freq1.values()) == sorted(freq2.values())


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        c1, c2 = Counter(word1), Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        """
        word1 = "aabbccc"
        c1 = {'a': 2, 'b': 2, 'c': 3} -> Counter()
        c1.values() -> [2, 2, 3]
        Counter(c1.values()) -> Counter({2: 2, 3: 1})

        i.e. '2' appears 2 times, '3' appears 1 time.
        """

        return Counter(c1.values()) == Counter(c2.values())
