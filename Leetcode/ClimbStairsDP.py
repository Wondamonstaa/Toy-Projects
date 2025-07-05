class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        
        def fib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        
        return fib(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n=4:
        1*4=4
        1*2+2*2=4
        2*2=4
        2*2+1*2=4
        """

        def fib(i):
            if i == n:
                return 1
            if i > n:
                return 0
            return fib(i+1) + fib(i+2)
        
        return fib(0)
