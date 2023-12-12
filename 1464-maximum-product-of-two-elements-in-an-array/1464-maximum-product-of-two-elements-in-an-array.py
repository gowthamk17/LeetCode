class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = -1
        second = -1
        for n in nums:
            if n > first:
                second = first
                first = n
            elif n > second:
                second = n
        return (first-1) * (second -1)