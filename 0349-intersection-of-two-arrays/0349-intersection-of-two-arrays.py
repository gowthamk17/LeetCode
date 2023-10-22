class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for n in nums1:
            if n in nums2 and n not in result:
                result.append(n)       
        return result