class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        for n in nums1:
            if n in nums2 and n not in ans:
                ans.append(n)
        for n in nums2:
            if n in nums3 and n not in ans:
                ans.append(n)
        for n in nums3:
            if n in nums1 and n not in ans:
                ans.append(n)
        return ans