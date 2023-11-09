class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        for n in set1:
            if n in set2 and n not in ans:
                ans.append(n)
        for n in set2:
            if n in set3 and n not in ans:
                ans.append(n)
        for n in set3:
            if n in set1 and n not in ans:
                ans.append(n)
        return ans