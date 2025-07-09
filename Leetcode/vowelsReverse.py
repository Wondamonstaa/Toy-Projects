class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""

        vowels = set('aeiouAEIOU')
        s1 = list(s)
        i, j = 0, len(s1) - 1

        while i < j:
            if s1[i] not in vowels:
                i += 1
                continue
            if s1[j] not in vowels:
                j -= 1
                continue
            s1[i], s1[j] = s1[j], s1[i]
            i += 1
            j -= 1

        return ''.join(s1)
