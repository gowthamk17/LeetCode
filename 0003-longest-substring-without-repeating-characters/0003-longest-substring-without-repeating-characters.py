class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        left = 0
        charSet = set()
        for right in range(n):
            if s[right] in charSet:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
            else:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
        return maxLength