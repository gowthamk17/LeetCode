class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def valid(i):
            if len1 % i or len2 % i:
                return False
            n1, n2 = len1//i, len2//i
            prefix = str1[:i]
            return str1 == n1 * prefix and str2 == n2 * prefix
        for i in range(min(len1,len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""