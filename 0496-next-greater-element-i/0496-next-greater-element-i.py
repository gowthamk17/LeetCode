class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            for i in range(len(nums2)):
                if n == nums2[i]:
                    nextBig = False
                    for j in range(i, len(nums2)):
                        if n < nums2[j]:
                            ans.append(nums2[j])
                            nextBig = True
                            break
                    if not nextBig:
                        ans.append(-1)
        return ans
                    