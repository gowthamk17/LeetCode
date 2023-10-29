class Solution:
    def __init__(self):
        self.d = {0:0, 1:1}
    
    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        else:
            return self.fib(n-1) + self.fib(n-2)
        