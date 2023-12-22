class Solution:
    def maxScore(self, s: str) -> int:
        one_count = 0
        for c in s:
            if c == '1':
                one_count += 1
        max_score = -1
        zero_count = 0
        for i in range(len(s)-1):
            c = s[i]
            if c == "0":
                zero_count += 1
            else:
                one_count -= 1
            max_score = max(max_score, zero_count + one_count)
        return max_score