class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start <= end:
            mid = (start+end)//2
            sqr = mid*mid
            if sqr > num:
                end = mid-1
            elif sqr < num:
                start = mid+1
            elif sqr == num:
                return True
        return False
            