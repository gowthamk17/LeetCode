class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        i = sys.maxsize
        j = sys.maxsize
        for l in range(len(nums)):
            if nums[l] <= i:
                i = nums[l]
            elif nums[l] <= j:
                j = nums[l]
            else:
                return True
        return False
        