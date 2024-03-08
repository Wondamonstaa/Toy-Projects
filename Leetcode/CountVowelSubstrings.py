class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def isVowel(c):
            return c in 'aeiou'
        
        def allVowelsPresent(substring):
            return all(vowel in substring for vowel in 'aeiou')
        
        count = 0
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                substring = word[start:end]
                # Check if the substring contains only vowels and all vowels are present
                if all(isVowel(c) for c in substring) and allVowelsPresent(substring):
                    count += 1
                    
        return count
