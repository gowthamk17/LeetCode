class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(int(columnNumber % 26) + ord('A')) + ans
            columnNumber = columnNumber // 26
        return ans