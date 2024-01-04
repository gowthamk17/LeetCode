class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for n in counter.values():
            if n == 1:
                return -1
            res += ceil(n / 3)
        return res