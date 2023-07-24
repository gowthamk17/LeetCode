class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempSet = set()
        for i in range(len(nums)):
            if nums[i] in tempSet:
                tempSet.remove(nums[i])
            else:
                tempSet.add(nums[i])
        return tempSet.pop()
        