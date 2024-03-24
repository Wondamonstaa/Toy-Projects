class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        
        def fib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        
        return fib(n)
