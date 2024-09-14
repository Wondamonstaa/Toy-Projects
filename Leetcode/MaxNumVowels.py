class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        if not s:
            return 0
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        count = 0
        maxi = 0
        i = 0

        '''while i < n:
        
            window = s[i:k]
            count = sum(1 for char in window if char in vowels)

            if count <= k and count > maxi:
                maxi = count
                  
            i += 1
            k += 1'''
        
        # The first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxi = count

        # Slide from left to right
        for i in range(k, n):
            if s[i] in vowels:  # Add the new character at the right end of the window
                count += 1
            if s[i - k] in vowels:  # Remove the character that's left behind as the window slides
                count -= 1
            maxi = max(maxi, count)  # Update the maximum count of vowels

        return maxi
