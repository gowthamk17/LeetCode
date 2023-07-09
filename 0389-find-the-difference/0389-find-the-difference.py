class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if c in s:
                s = s.replace(c, "", 1)
            else:
                return c
        