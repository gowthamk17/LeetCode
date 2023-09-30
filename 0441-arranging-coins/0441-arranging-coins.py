class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairs = 0
        i = 1
        while n > 0:
            if n >= i:
                stairs += 1
            n -= i
            i += 1
        return stairs