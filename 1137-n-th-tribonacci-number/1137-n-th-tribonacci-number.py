class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0,1,1]
        if n <= 2:
            return cache[n]
        f, s ,t = 0, 1, 1
        for i in range(3, n+1):
            ne = f + s + t
            f, s, t = s, t, ne
        return t