class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        word = []
        v = []

        for char in s:
            if char in vowels:
                v.append(char)
                word.append('ч')
            else:
                word.append(char)

        for i in range(len(word)):
            if word[i] == 'ч' and v:
                word[i] = v.pop()

        return "".join(word)
