class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        large = nums1
        small = nums2
        if len(large) < len(small):
            large = nums2
            small = nums1
        for n in small:
            if n in large:
                result.append(n)
                large.remove(n)
        return result