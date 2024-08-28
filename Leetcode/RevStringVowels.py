class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)  
        
        vowels_list = [char for char in s if char in vowels]
        
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowels_list.pop()
        
        return ''.join(s_list)
