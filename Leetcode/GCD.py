from math import gcd 

class Solution:

    def gcd(self, a: int, b: int) -> int:

        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums: List[int]) -> int:
        
        a: int = min(nums)
        b: int = max(nums)
        #gcd = self.gcd(b, a)

        return gcd(a,b)


import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if not str1:
            return str2

        if not str2:
            return str1

        if str1 + str2 != str2 + str1:
            return ""

        gcd = math.gcd(len(str1), len(str2))

        return str1[:gcd] if len(str1) > len(str2) else str2[:gcd]
