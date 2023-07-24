class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempList = []
        for i in range(len(nums)):
            if nums[i] in tempList:
                tempList.remove(nums[i])
            else:
                tempList.append(nums[i])
        return tempList[0]
        