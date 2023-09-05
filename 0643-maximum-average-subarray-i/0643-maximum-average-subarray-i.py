class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        res = total
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            res = max(res,total)
        return res/k