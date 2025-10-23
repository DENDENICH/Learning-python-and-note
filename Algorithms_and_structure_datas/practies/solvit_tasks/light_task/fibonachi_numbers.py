from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n < 3:
            return 0 if n < 1 else 1
        return self.fib(n - 1) + self.fib(n - 2)
    

solution = Solution()

result = solution.fib(4)
print(result)
