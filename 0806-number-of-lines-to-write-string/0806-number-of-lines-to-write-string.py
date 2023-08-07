class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 0
        lineWidth = 0
        for c in s:
            charWidth = widths[ord(c) - ord('a')]
            if (charWidth + lineWidth) > 100:
                lines += 1
                lineWidth = charWidth
            else:
                lineWidth += charWidth
        lines += 1
        return [lines, lineWidth]
        