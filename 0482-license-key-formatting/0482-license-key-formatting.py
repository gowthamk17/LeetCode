class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        result = ''
        count = 0
        for i in range(len(s)):
            if s[i] != '-':
                result += s[i].upper()
                count += 1
                if count == k:
                    result += '-'
                    count = 0
        if len(result) > 0 and result[-1] == '-':
            result = result[:len(result) - 1]             
        return result[::-1]