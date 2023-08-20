class Solution:
    def mySqrt(self, x: int) -> int:
        # intuition
        if  x < 2:
            return x
        sqrt = 0
        for i in range(1, x):
            if i * i <= x:
                sqrt = i
            else:
                break;
        return sqrt