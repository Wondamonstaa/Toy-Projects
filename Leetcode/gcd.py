class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to calculate GCD of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # If concatenating str1 + str2 is not equal to str2 + str1, they don't have a common divisor
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd_length from str1
        return str1[:gcd_length]
