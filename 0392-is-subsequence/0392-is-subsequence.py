class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        for c in t:
            if not s:
                break
            if c == s[0]:
                s = s[1:]
        if s:
            return False
        else:
            return True
        