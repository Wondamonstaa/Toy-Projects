class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words: List[str] = [word.strip() for word in s.split()]

        return len(words[len(words)-1])
