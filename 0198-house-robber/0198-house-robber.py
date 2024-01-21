class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0, 0
        for n in nums:
            curr, prev = prev, curr
            curr = max(curr+n, prev)
            
        return curr