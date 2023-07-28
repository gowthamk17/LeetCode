class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) == 1:
            return ord(columnTitle) + 1 - ord('A')
        else:
            ans = 0
            for i in range(len(columnTitle)):
                digit = (26 ** i) * (ord(columnTitle[len(columnTitle) - 1 - i]) - ord('A') + 1)
                ans += digit
            return ans