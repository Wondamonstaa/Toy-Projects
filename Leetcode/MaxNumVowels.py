class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        if not s:
            return 0
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        count = 0
        maxi = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
            maxi = count

        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            maxi = max(maxi, count)

        return maxi
