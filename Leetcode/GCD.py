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
