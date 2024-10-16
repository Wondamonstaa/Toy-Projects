class Solution:

    def gcd(self, a, b) -> int:

        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""

        a = min(len(str1), len(str2))
        b = max(len(str1), len(str2))

        gcd = self.gcd(a, b)
        print(gcd)

        return str2[:gcd]
