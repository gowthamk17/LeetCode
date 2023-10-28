class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        for i in range(1, s_len // 2 + 1):
            if s_len % i == 0:
                subStr = s[:i]
                if subStr * (s_len // i) == s:
                    return True
        return False