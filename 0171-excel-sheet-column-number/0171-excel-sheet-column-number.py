class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        if len(columnTitle) == 1:
            return ord(columnTitle) + 1 - ord('A')
        else:
            titleStr = columnTitle[::-1]
            for i in range(len(titleStr)):
                digit = (26 ** i) * (ord(titleStr[i]) + 1 - ord('A'))
                ans += digit
            return ans