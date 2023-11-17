class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_pair_sum = -1
        size = len(nums)
        for i in range(size//2):
            pair_sum = nums[i] + nums[size-i-1]
            max_pair_sum = max(pair_sum, max_pair_sum)
        return max_pair_sum