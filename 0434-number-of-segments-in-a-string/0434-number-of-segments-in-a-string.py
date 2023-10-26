class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        seg = False
        for c in s:
            if c == ' ':
                if seg:
                    count += 1
                    seg = False
            else:
                seg = True
        if seg:
            count += 1
        return count